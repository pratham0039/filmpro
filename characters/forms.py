from django import forms

class SceneDurationRemarkForm(forms.Form):
    duration = forms.CharField(max_length=255)
    remark = forms.CharField(widget=forms.Textarea, required=False)
    lenscs = forms.CharField(widget=forms.Textarea, required=False)
    notescs = forms.CharField(widget=forms.Textarea, required=False)
    shotno = forms.IntegerField(widget=forms.Textarea, required=False)
