from django import forms
from .models import Cpu

class CpuForm(forms.ModelForm):
	class Meta:
		model = Cpu
		fields = ['cpu','photo']