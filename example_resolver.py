

def get_anno_details(arguments):

    details = {'width': arguments.get('width'), 'height': arguments.get('height')}

    canvas_1, canvas_2 = arguments.get('canvas').split('--')
    details['canvasURI'] = "http://waylon.digirati.com/work/" + canvas_1 + "/canvas/" + canvas_2

    details['imageURI'] = "https://dlcs.io/iiif-img/50/1/" + arguments.get('image')

    details['annotationBaseURI'] = "http://waylon.digirati.com/work/" + arguments.get('anno') + "/annos/contentAsText/{{line_number}}"

    return details
