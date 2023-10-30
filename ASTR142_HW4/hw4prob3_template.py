#
# (c) 2023 Michael Fitzgerald (mpfitz@ucla.edu)
#
# Some code for querying the virtual observatory to make finder charts
#


# SkyView Attempt 

SkyView.get_image_list(position='M2', survey=['Optical:SDSS']
        # Source: https://skyview.gsfc.nasa.gov/current/cgi/titlepage.pl

# Simple Image Access (SIA) Protocol
>>> jhu_dr7_service = [s for s in services if 'SDSSDR7' in s.short_name and'jhu' in s.ivoid][0]
>>> sdss_table_jhu = jhu_dr7_service.search(pos=coords, size=0.2, format=None)
>>> sdss_table_jhu.to_table().show_in_notebook(display_length=5)

>>> file_name=download_file(sdss_table_jhu[6].getdataurl(), cache=True, timeout=600)
>>> hdu_list = fits.open(file_name)
>>> plt.imshow(hdu_list[0].data, cmap='gray', origin='lower', vmax=1200, vmin=1010)
# Source: https://nasa-navo.github.io/navo-workshop/CS_Image_Access.html

# Source: http://aladin.cds.unistra.fr/AladinLite/


import pyvo as vo
import matplotlib as mpl
import pylab


# set up VO service for DSS image retrieval

# set up VO service for IRSA 2MASS point-source catalog retrieval


# loop over sources


    # compute object coordinates


    # retrieve image


    # retrieve point sources


    # set up figure
    fig = pylab.figure(0)
    fig.clear()
    ax = fig.add_subplot(111)

    # display image
    ax.imshow(imdata,
              cmap=mpl.cm.gray,
              interpolation='nearest',
              )

    # display point sources
    ax.scatter()


    # annotate


    # save figure
