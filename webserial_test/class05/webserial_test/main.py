import js as p5
from js import document

data = None

def setup():
  p5.createCanvas(300, 300)
  print('hello p5!')
  p5.rectMode(p5.CENTER)

def draw():
  p5.background(255)

  global data
  data = document.getElementById("data").innerText
  
  circle_size = int(data)
  p5.noStroke()
  p5.fill(150, 0, 0)
  p5.push()
  angle = p5.radians(data)
  p5.translate(150, 150)
  p5.rotate(angle)
  p5.rect(0, 0, circle_size, circle_size)
  p5.pop()
  
def print_test(x):
  print(x)

  
