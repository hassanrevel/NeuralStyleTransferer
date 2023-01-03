from PIL import Image
from io import BytesIO
import torch
import torchvision.transforms as transforms
import requests

device = 'cuda' if torch.cuda.is_available() else 'cpu'

imsize = 512 if torch.cuda.is_available() else 128

loader = transforms.Compose([
    transforms.Resize(imsize),  # scale imported image
    transforms.ToTensor()])  # transform it into a torch tensor


def image_loader_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)


def image_loader_dir(path):
    image = Image.open(path)
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)


def load_img_style(img_url=None, style_url=None, img_dir=None, style_dir=None):

    if img_url:
        content_img = image_loader_url(img_url)
        style_img = image_loader_url(style_url)

        return content_img, style_img

    if img_dir:
        content_img = image_loader_dir(img_dir)
        style_img = image_loader_url(style_dir)
        return content_img, style_img