import imgkit

options = {
    'format': 'png',
    'encoding': 'UTF-8',
    'width': 1366,
    'height': 768 ,
    'quality': 80 
}

imgkit.from_url('https://google.com', 'out.png', options=options)
