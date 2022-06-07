from django.shortcuts import render, redirect
from django.http import Http404
from app_page_cap_img.models import PageCapImage, Configuracao
from app_page_cap_img.models import LeadsEmail
from django.core.mail import send_mail
from pagecapimg import settings
import time



def modeloPageCap(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":  #POST method
        # print(request.POST)
        new_email = request.POST.get("email")
        new_lead = LeadsEmail(email=new_email)
        new_lead.save()

        return redirect('url_download')
    else:  # GET method
        print('\n\n ENTROU AQUI \n\n')
        data_conf = {}
        data_conf['config'] = Configuracao.objects.all()

        for d in data_conf['config']:
            tipo_media = d.tipo_media
            position = d.media_position

        # ------------------------------------------------------------
        # FINDING THE CONFIGURATION SETED BY USER IN THE DASHBOARD
        #-------------------------------------------------------------
        if tipo_media is "I" and position is "E":  # imagem à esquerda
            data = {}
            data['title'] = 'Home Captura | Imagem'
            data['posicao'] = 'E'
            data['dados'] = PageCapImage.objects.all()
            return render(
                request,
                'app_page_cap_img/pageImgEsq_Dir.html',
                data
            )

        if tipo_media is 'I' and position is 'D':  # imagem à direita
            data = {}
            data['title'] = 'Home Captura | Imagem'
            data['posicao'] = 'D'
            data['dados'] = PageCapImage.objects.all()
            return render(
                request,
                'app_page_cap_img/pageImgEsq_Dir.html',
                data
            )

        if tipo_media is 'V' and position is 'E':  # video à esquerda
            data = {}
            data['title'] = 'Home Captura | Video'
            data['posicao'] = 'E'
            data['dados'] = PageCapImage.objects.all()
            return render(
                request,
                'app_page_cap_img/pageVideoEsq_Dir.html',
                data
            )

        if tipo_media is 'V' and position is 'D':  # video à direita
            data = {}
            data['title'] = 'Home Captura | Video'
            data['posicao'] = 'D'
            data['dados'] = PageCapImage.objects.all()
            return render(
                request,
                'app_page_cap_img/pageVideoEsq_Dir.html',
                data
            )
        else:
            pass


def download(request):
    subject = 'Teste | envio email python'
    message = 'Olá, este é um teste de django enviando email.'
    author_email = settings.EMAIL_HOST_USER
    to_email = LeadsEmail.objects.last()
    time.sleep(3)
    print('\n\n Ultimo email: {}'
        .format(to_email)
    )
    to_list = [to_email, settings.EMAIL_HOST_USER]

    send_mail(
        subject,
        message,
        author_email,
        to_list,
        fail_silently=True   # True
    )

    print("""

         ENVIEI EMAIL PRA VC

        """)

    return redirect('url_home')
