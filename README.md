# pydeface-gear

A flywheel gear to remove facial structure from MRI images.

Leverages [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL),
[Python 3](https://www.python.org/downloads/),
[NumPy](http://www.numpy.org/),
[NiBabel](http://nipy.org/nibabel/), and 
[Nipype](http://nipype.readthedocs.io/en/latest/) 
to coregister a provided image to a template and removes facial features by removing the facial structure in accordance with the registration template and face mask.  User may provide a template and face mask.

## Website

The source code of pydeface can be found at [github](https://github.com/poldracklab/pydeface)

## Usage Notes

### inputs

* infile (required): The NIfTI file to remove facial structure from
* template (optional): The optional template image that will be used as the registration target instead of the default.
* facemask (optional): The optional face mask image that will be used instead of the default.

### parameters

* cost: FSL-FLIRT cost function. "mutualinfo" default.
* nocleanup: Do not cleanup temporary files. Off by default.
* verbose: Show additional status prints. Off by default.