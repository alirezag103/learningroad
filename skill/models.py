from django.db import models
import uuid

# Create your models here.

class SkillCategory(models.Model):

    # shall we set primary_key=True for title?
    title = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey("self", null=True, on_delete=models.PROTECT, related_name='+')
    description = models.CharField(max_length=255)


class Skill(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title',], name='unique_skill_title')
        ]


class Prerequisite(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    HIGH_SIGNIFICANCE = 'H'
    MEDIUM_SIGNIFICANCE = 'M'
    LOW_SIGNIFICANCE = 'L'
    SIGNIFICANCE_LEVELS = [
        (HIGH_SIGNIFICANCE, 'High'),
        (MEDIUM_SIGNIFICANCE,'Medium'),
        (LOW_SIGNIFICANCE, 'Low'),
    ]
    significance = models.CharField(max_length=1, choices=SIGNIFICANCE_LEVELS, default=MEDIUM_SIGNIFICANCE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='+')
    requisite = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='+')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['skill', 'requisite',], name='unique_skill_prerequisite')
        ]



