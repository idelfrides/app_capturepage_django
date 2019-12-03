from django.db import models
from django.conf import settings
from .managers import Manager

POSITION_CHOICES =  (
    ('E', 'Esquerda'),
    ('D', 'Direita')
)

TYPE_MIDEA_CHOICES = (
    ('I', 'Imagem'),
    ('V',  'Vídeo')
)

class PageCapImage(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        default=1, 
        on_delete=models.CASCADE
    )

    material = models.CharField(
        max_length=100, 
        default='E-book vendas online'
    )

    headline = models.TextField(
        default='Coloque sua Headline aqui.'
    )

    copy_descricao = models.TextField(
        default='Sua Copy descrição aqui.'
    )

    image = models.ImageField(
        upload_to='images/', 
        null=True, 
        blank=True
    )

    update = models.DateTimeField(
        auto_now=True, 
        auto_now_add=False
    )
    
    timestamp = models.DateTimeField(
        auto_now=False, 
        auto_now_add=True
    )

    def __str__(self):
        return self.material

    class Meta:
        verbose_name_plural = 'Material'


class Configuracao(models.Model):

    tipo_media =  models.CharField(
        choices=TYPE_MIDEA_CHOICES, 
        default='Imagem', 
        max_length=20
    )
    media_position = models.CharField(
        choices=POSITION_CHOICES, 
        default='Esquerda', 
        max_length=20
    )
    update = models.DateTimeField(
        auto_now=True, 
        auto_now_add=False
    )
    timestamp = models.DateTimeField(
        auto_now=False, 
        auto_now_add=True
    )

    def __str__(self):
        n = "Configurações"
        return n

    class Meta:
        verbose_name_plural = 'Configuracoes'


class Media(models.Model):
    imagem = models.ImageField(upload_to='images/')

    video = models.FileField(
        upload_to='videos/', 
        null=True, 
        blank=True
    )
 
    arquivo_pdf = models.FileField(upload_to='files/')
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        # man = Manager()
        # c = man.set_count(1)
        nome = "Media"  # + str(self.count)
        return nome

    class Meta:
        verbose_name_plural = 'Medias'

    # def get_absolute_url(self):
    #    return "app_name/%s/" %(self.id)


class LeadsEmail(models.Model):

    email = models.EmailField(
        default='idelfridesjorge@alu.ufc.br'
    )
    
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email