from src.Model.model import get_style_model_and_losses, cnn
from src.Model.utils import get_input_optimizer, cnn_normalization_std, cnn_normalization_mean
from src.data import load_img_style
from src.visualize import imshow
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-iu', '--img_url', default=None,
    type=str,
    required=False
)
parser.add_argument(
    '-su', '--style_url', default=None,
    type=str,
    required=False
)
parser.add_argument(
    '-id', '--img_dir',
    default=None,
    type=str,
    required=False
)
parser.add_argument(
    '-sd', '--style_dir',
    default=None,
    type=str,
    required=False
)
parser.add_argument(
    '-od', '--out_dir',
    default=None,
    type=str,
    required=False
)
args = parser.parse_args()

def run_style_transfer(cnn, normalization_mean, normalization_std,
                       content_img, style_img, input_img, num_steps=300,
                       style_weight=1000000, content_weight=1):
    """Run the style transfer."""
    print('Building the style transfer model..')
    model, style_losses, content_losses = get_style_model_and_losses(cnn,
        normalization_mean, normalization_std, style_img, content_img)
    optimizer = get_input_optimizer(input_img)

    print('Optimizing..')
    run = [0]
    while run[0] <= num_steps:

        def closure():
            # correct the values of updated input image
            input_img.data.clamp_(0, 1)

            optimizer.zero_grad()
            model(input_img)
            style_score = 0
            content_score = 0

            for sl in style_losses:
                style_score += sl.loss
            for cl in content_losses:
                content_score += cl.loss

            style_score *= style_weight
            content_score *= content_weight

            loss = style_score + content_score
            loss.backward()

            run[0] += 1
            if run[0] % 50 == 0:
                print("run {}:".format(run))
                print('Style Loss : {:4f} Content Loss: {:4f}'.format(
                    style_score.item(), content_score.item()))
                print()

            return style_score + content_score

        optimizer.step(closure)

    # a last correction...
    input_img.data.clamp_(0, 1)

    return input_img


content_img, style_img = load_img_style(
    img_url=args.img_url,
    style_url=args.style_url,
    img_dir=args.img_dir,
    style_dir=args.style_dir
    )
input_img = content_img.clone()

output = run_style_transfer(
    cnn, cnn_normalization_mean, cnn_normalization_std,
                            content_img, style_img, input_img)


plt.figure()
imshow(output, title='Output Image')
# sphinx_gallery_thumbnail_number = 4
plt.ioff()
plt.show()