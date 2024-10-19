from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

from django.shortcuts import render
from django.db.models import Q 
from .models import Contact 



def contact_list(request):
    query = request.GET.get('q', '')  
    address_query = request.GET.get('address', '')  
    # Start with all contacts
    contacts = Contact.objects.all()  

    # Filter contacts based on the search queries
    if query:
        contacts = contacts.filter(name__icontains=query)  # Search by name

    if address_query:
        contacts = contacts.filter(address__icontains=address_query)  # Search by address
        
    # Return the context to the template
    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts,
        'query': query,
        'address_query': address_query,  # Pass the address query to the template
    })

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
