import hashlib
import settings


def get_anno_details(arguments):

    details = {
        'width': arguments.get('width'),
        'height': arguments.get('height'),
        'canvasURI': arguments.get('canvas'),
        'imageURI': arguments.get('image'),
        'annotationBaseURI': settings.ANNOTATION_BASE + "/anno/" + hashlib.md5(
                   arguments.get('canvas')).hexdigest() + "/{{line_number}}"
    }

    return details
