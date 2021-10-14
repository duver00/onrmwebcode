from .models import ControlInterno, LinksExternos, DocumentosRectores
from eventos.models import EventosModel
from noticias.models import Post


def base_footer(request):
    nownews = Post.objects.all().last()
    nowevents = EventosModel.objects.all().last()
    last = 'ads'
    if nowevents.created > nownews.created:
        last = nowevents
    else:
        last = nownews
    links = LinksExternos.objects.all()
    control = ControlInterno.objects.all()
    rectores = DocumentosRectores.objects.all()
    return {'now': nownews, 'nowevent': nowevents, 'links': links, 'control': control, 'rectores': rectores,
            'last': last}
