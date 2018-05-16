import random
import io

from flask import Flask, make_response, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


app = Flask(__name__)

# @app.route('/plot.png')
# def plot():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)

#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]

#     axis.plot(xs, ys)
#     canvas = FigureCanvas(fig)
#     output = io.BytesIO()
#     canvas.print_png(output)
#     response = make_response(output.getvalue())
#     response.mimetype = 'image/png'
#     return response

@app.route('/fig')

def fig():
    #fig = draw_polygons(cropzonekey)
    fig = plt.plot([1,2,3,4], [1,2,3,4])
    #img = StringIO()
    img = io.BytesIO()
    #fig.savefig(img)
    plt.savefig(img)
    img.seek(0)
    return render_template('test.html', data=img)

if __name__ == '__main__':
    app.run(debug=True)