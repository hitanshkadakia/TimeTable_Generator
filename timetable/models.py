from django.db import models
from accounts.models import Faculty

# Create your models here.
class Subject(models.Model):
    """Model definition for Subject."""

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=254)
    semester = models.PositiveSmallIntegerField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),)
    )

    class Meta:
        """Meta definition for Subject."""

        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        """Unicode representation of Subject."""
        return self.name


class Subject_Assigned(models.Model):
    """Model definition for Subject_Assigned."""

    room = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=50, blank=True, null=True, default=None)

    class Meta:
        """Meta definition for Subject_Assigned."""

        verbose_name = "Subject_Assigned"
        verbose_name_plural = "Subject_Assigned"

    def __str__(self):
        """Unicode representation of Subject_Assigned."""
        return self.subject.name + " | sem: " + str(self.subject.semester)


class TimeTable(models.Model):
    """Model definition for TimeTable."""

    day = models.CharField(
        choices=(
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
            ("Sunday", "Sunday"),
        ),
        max_length=50,
    )
    semester = models.PositiveSmallIntegerField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8))
    )
    period1 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period1",
    )
    period2 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period2",
    )
    period3 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period3",
    )
    period4 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period4",
    )
    period5 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period5",
    )
    period6 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period6",
    )
    period7 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period7",
    )
    period8 = models.ForeignKey(
        Subject_Assigned,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="period8",
    )

    class Meta:
        """Meta definition for TimeTable."""

        verbose_name = "TimeTable"
        verbose_name_plural = "TimeTables"

    def __str__(self):
        """Unicode representation of TimeTable."""
        return self.day + " | " + str(self.semester)
