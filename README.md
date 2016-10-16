# quantmethods
here lies the code for my thesis

synch.py takes  a folder with 6 sets of answers, returns a .csv where every line is a collection of all answers to a respectful picture in the test sample
 3darray_and_sorting.py, it takes that doc and also all the pictures in all the folders (well, not the pictures themselves, but their flienames). reg_count.py is called by it. if you uncomment a line, it may also call synch.py to update the main textfile.
since i used different interpreters (3.4 and anaconda 3.5 for matplotlib's sake) there is no such thing as call the results from radplot.py. You'd have to run 3darray_and_sorting with handset parameters (no. of the component, 0:2), but there's no need for it: they are manually pasted inside the script. when you open the script, they'd be softwrapped, so your computer won't be overloaded. 
Heatmap.py is neither working, nor finished, since there appear to be to few points on a 2d projection of the 3d array for a decent heatmap. 
