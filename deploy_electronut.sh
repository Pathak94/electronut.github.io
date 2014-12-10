echo ****uploading site***

rsync -crv -e ssh --rsync-path=~/bin/rsync _site/ elec7045@electronut.in:html/

# play sound
afplay /System/Library/Sounds/Basso.aiff 
