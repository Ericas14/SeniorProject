# SeniorProject
1. Members: Jordan Holeman. Kennedy Marsh, and Erica Smith
2. Product Description
   1. In today's world, many different types of documents, ranging from forms,
invoices, bank statements, mail, etc., contain machine printed and handwritten 
text in the same document image. Since the algorithms created to recognize machine-printed
texts and handwritten texts are different, it is necessary to distinguish between these two 
types of text before giving it to OCR systems. Optical character recognition systems (OCR), 
are the electronic conversion of images of typed, handwritten or printed text into machine-encoded text.
It is used as a form of data entry from printed paper data records, and it is a common method of digitizing 
printed texts so that they can be electronically edited, searched, stored more compactly, and used in machine processes 
like cognitive computing, machine translation, and extracted text-to-speech. With this project, we aim to maximize the accuracy and efficiency of OCRs.
3. Product Scope
   1. Although there are many different mythologies used for performing optical character recognition (OCR) on handwritten 
text and machine printed text,this new invention will be more efficient. Presently, there are inventions that can distinguish 
handwritten text and machine text with extracting contours, structural and statistical features or, dividing text blocks into 
horizontal or vertical directions to classify the text according to variance, or the total number of horizontal, vertical and slanted strokes in text, 
etc. However, this new invention uses a new method which is to enclose each connected component within a rectangular or bounding box and computing its 
height and width to get the sum and the maximum horizontal run. The sum is all the pixels corresponding to the connected component and the horizontal run 
is the longest consecutive number of horizontal pixels in the corresponding connected component. This invention will then identify connected components that 
are suspected of being characters to see if it is less than or equal to a first user-definable number. Today, a patent is assigned by the National Security Agency for this invention. 
However, the patent is not yet implemented. As a result, this research project will lead to handwritten and machine printed images being distinguished more accurately compared to other OCRs.
4. User Tutorial
   1. Click Upload File on GUI
   2. Choose files (.jpg or .png) from the computer
   3. Click open after files are chosen
   4. Wait for GUI to print out results
   5. To view results, look under Verdict next to each image’s path which is
      printed underneath the upload file button
5. Installation Guide 
   1. Install PyCharm
   2. Open PyCharm
   3. In PyCharm, click File
   4. Under File, Open seniorprojectredo.py
