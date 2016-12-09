from flask import Flask, request, Response, stream_with_context, jsonify
import settings
import requests
import logging
import json
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
resolver = __import__(settings.RESOLVER)


def main():

    app.run(threaded=True, debug=True, port=5051, host='0.0.0.0')


@app.route('/annotations/line/', methods=['GET'])
def annotations():

    resources = []
    args = request.args
    info = resolver.get_anno_details(args)

    req = requests.get(url=settings.STARSKY, params={"imageURI": info.get("imageURI"), "width": info.get("width"),
                                                     "height": info.get("height")})

    if req.status_code is not 200:
        logging.error("Could not obtain line info from starsky")
        raise IOError("Could not obtain line info from starsky")

    body = req.json()
    count = 0
    for line in body["lines"]:
        resources.append(annotation_for_line(line, count, info))
        count += 1

    annotation_list = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@id": request.url,
        "@type": "sc:AnnotationList",
        "resources": resources,
    }

    return jsonify(annotation_list)


def annotation_for_line(line, count, info):

    annotation = {
        "@id": info['annotationBaseURI'].replace("{{line_number}}", str(count)),
        "@type": "oa:Annotation",
        "motivation": "sc:painting",
        "resource": {
            "@type": "cnt:ContentAsText",
            "format": "text/plain",
            "chars": line["text"],

        },
        "on": info.get("canvasURI") + "#xywh=" + line["xywh"]
    }

    return annotation


def set_logging():
    logging.basicConfig(filename="river_annotations_service.log",
                        filemode='a',
                        level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', )
    logging.getLogger('boto').setLevel(logging.ERROR)
    logging.getLogger('botocore').setLevel(logging.ERROR)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)


if __name__ == "__main__":
    main()



