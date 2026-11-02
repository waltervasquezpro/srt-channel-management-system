from django.db import models
from django.contrib.auth.models import User


# -----------------------------
# CUSTOMER
# -----------------------------
class Customer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# -----------------------------
# CHANNEL
# -----------------------------
class Channel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# -----------------------------
# SERVER (kept for now, but not used in Service)
# -----------------------------
class Server(models.Model):
    hostname = models.CharField(max_length=150, unique=True)
    site = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["hostname"]

    def __str__(self):
        return f"{self.hostname} ({self.site})"


# -----------------------------
# SERVICE
# -----------------------------
class Service(models.Model):

    SERVICE_TYPE_CHOICES = [
        ("DELIVERY", "Delivery"),
        ("RECEIVE", "Receive"),
    ]

    PROTOCOL_CHOICES = [
        ("SRT", "SRT"),
        ("HLS", "HLS"),
        ("RTMP", "RTMP"),
    ]

    MODE_CHOICES = [
        ("CALLER", "Caller"),
        ("LISTENER", "Listener"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("TEST", "Test"),
        ("REMOVED", "Removed"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT)

    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES)
    protocol = models.CharField(max_length=10, choices=PROTOCOL_CHOICES)

    
    public_ip = models.CharField(max_length=255)
    port = models.IntegerField()

    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["public_ip", "port"],
                name="unique_service_ip_port",
            )
        ]

    def __str__(self):
        return f"{self.customer} - {self.channel} - {self.public_ip}:{self.port}"

    @property
    def test_expired(self):
        from django.utils import timezone
        return self.status == "TEST" and (timezone.now() - self.created_at).days >= 7