from django.db import models

class JobDescription(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')
    extracted_text = models.TextField(blank=True)
    match_score = models.FloatField(null=True, blank=True)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE, related_name='resumes')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"

