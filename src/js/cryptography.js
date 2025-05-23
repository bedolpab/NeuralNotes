const notesGrid = document.getElementById('notes-grid');
const previewPane = document.getElementById('preview-pane');

const directory = "../cnotes/";
const prefix = "c_note_";
let index = 0;
let imagesLoaded = 0; 

function loadNextImage() {
  const src = `${directory}${prefix}${index}.png`;
  const img = new Image();
  
  img.onload = () => {
    const container = document.createElement('div');
    container.className = 'image-container';

    const imageTop = document.createElement('div');
    imageTop.className = 'image-top';

    const displayedImg = document.createElement('img');
    displayedImg.src = src;
    displayedImg.alt = `Note ${index}`;
    imageTop.appendChild(displayedImg);

    const imageBottom = document.createElement('div');
    imageBottom.className = 'image-bottom';
    imageBottom.textContent = `[QC] Scanned Note [${index}]`;

    container.appendChild(imageTop);
    container.appendChild(imageBottom);

    container.addEventListener('click', () => {
      previewPane.innerHTML = `<img src="${src}" alt="Preview">`;
    });

    notesGrid.appendChild(container);

    imagesLoaded++;
    index++;
    loadNextImage();
  };

  img.onerror = () => {
    const emptyNotes = document.getElementById('preview-pane').querySelector("p");

    if (imagesLoaded === 0) {
      emptyNotes.innerText = "No Data to Show";
    } else {
      console.log('No more images after index', index - 1);
      emptyNotes.innerText = "Select data to show";
      console.log(index - 1);
    }
  };

  img.src = src;
}

loadNextImage();
