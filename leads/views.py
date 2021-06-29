from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render ,redirect , reverse
from django.http import HttpResponse
from .models import Lead , Agent
from .forms import LeadForm ,LeadModelForm
from django.views import generic

# Create your views here.
class LandingPage(generic.TemplateView):
    template_name = 'leads/landing.html'

class LeadListView(generic.ListView):
    queryset = Lead.objects.all()
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

class LeadDetailView(generic.DetailView):
    queryset = Lead.objects.all()
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) :
        return reverse('leads:lead-list')

    def form_valid(self, form):
        send_mail(
            subject='A new lead has been created',
            message='Please go to the Lead Application to check it',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView,self).form_valid(form)

def landing_page(request):
    return render(request , 'landing.html')

def lead_list(request):
    leads  = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request,'leads/lead_list.html' , context)

def lead_detail(request , pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request , 'leads/lead_detail.html' , context)



def lead_update(request , pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form  = LeadModelForm(request.POST , instance=lead)
            form.save()
            return redirect('/leads')
    context = {
        'form' : form,
        'lead' : lead
    }
    return render(request , 'leads/lead_update.html' , context)



def lead_create(request):
    form = LeadModelForm()
    if request.method=='POST':
        print("This is a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            '''print(form.cleaned_data)
            agent = form.cleaned_data['agent']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )
            print("The Lead is created successfully")'''
            form.save()
            return redirect('/leads')

    context={
        "form" : form
    }
    return render(request,'leads/lead_create.html' , context)


#def lead_create_submit(request):
    #return render(request , 'leads/lead_create_submit.html')


def lead_delete(request , pk):
    lead  = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
