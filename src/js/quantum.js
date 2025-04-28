const notesGrid = document.getElementById('notes-grid');
const previewPane = document.getElementById('preview-pane');

const directory = "../qnotes/";
const prefix = "qq_note_";
let index = 0;

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

    index++;
    loadNextImage();
  };

  img.onerror = () => {
    console.log('No more images after index', index - 1);
  };

  img.src = src;
}

loadNextImage();
