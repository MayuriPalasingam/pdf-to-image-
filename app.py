# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('sample.pdf',500,poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

file=open('page0.jpg',"rb")
image=file.read()
file.close()

image=bytearray(image)

key=48

for i,j in enumerate(image):
	image[i]=j^key

file=open("encripted.jpg","wb")	
file.write(image)
file.close()