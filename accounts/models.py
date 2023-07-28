from django.db import models

# Create your models here.
class Faculty(models.Model):
    """Model definition for Faculty."""

    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=254)
    subjects = models.TextField(default=None, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    gender = models.CharField(
        choices=(("male", "male"), ("female", "female")), max_length=10
    )
    designation = models.CharField(
        choices=(
            ("Professor", "Professor"),
            ("Assistant Professor", "Assistant Professor"),
            ("Associate Professor", "Associate Professor"),
            ("Head of the Department", "Head of the Department"),
            ("Guest Faculty", "Guest Faculty"),
        ),
        max_length=50,
    )

    class Meta:
        """Meta definition for Faculty."""

        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self):
        """Unicode representation of Faculty."""
        return self.name
