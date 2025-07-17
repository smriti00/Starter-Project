from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume
from .resume_parser import parse_resume
from .matcher import calculate_similarity
from django.contrib import messages

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume_text = parse_resume(resume.file.path)
            job_text = resume.job.description
            resume.extracted_text = resume_text
            resume.match_score = calculate_similarity(resume_text, job_text)
            resume.save()
            messages.success(request, f"Resume uploaded and scored: {resume.match_score:.2f}")
            return redirect('upload_resume')
    else:
        form = ResumeUploadForm()

    resumes = Resume.objects.all().order_by('-match_score')
    return render(request, 'upload_resume.html', {'form': form, 'resumes': resumes})

