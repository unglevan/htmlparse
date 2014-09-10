LINK="http://www.vnjpclub.com/"
wget \
     --recursive \ #get all file in LINK page
     --no-clobber \
     --page-requisites \
     -e robots=off \
      $LINK