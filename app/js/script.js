let books = JSON.parse(localStorage.getItem('misLibros')) || [];
let editIndex = null;

console.log('Libros cargados:', books);

function renderBooks() {
  const tabla = document.getElementById('booksTable');
  tabla.innerHTML = '';
  books.forEach((b, idx) => {
    let row = `
      <tr id="libro-${idx}">
        <td>${b.titulo}</td>
        <td>${b.autor}</td>
        <td>${b.anio}</td>
        <td>${b.estado}</td>
        <td>
          <button class="btnEditar" onclick="editarLibro(${idx})">Editar</button>
          <button class="btnEliminar" onclick="eliminarLibro(${idx})">Eliminar</button>
        </td>
      </tr>
    `;
    tabla.innerHTML += row;
  });
}

function saveToLocal() {
  localStorage.setItem('misLibros', JSON.stringify(books));
}

document.getElementById('btnAgregar').addEventListener('click', function () {
  let titulo = document.getElementById('titulo').value;
  let autor = document.getElementById('autor').value;
  let anio = document.getElementById('anio').value;
  let estado = document.getElementById('estado').value;

  if (titulo === '' || autor === '' || anio === '') {
    document.getElementById('msgForm').textContent =
      'Todos los campos son obligatorios';
    document.getElementById('msgExito').textContent = '';
    return;
  }

  books.push({ titulo, autor, anio, estado });
  saveToLocal();
  renderBooks();
  console.log('Libro agregado');

  document.getElementById('msgExito').textContent =
    'Libro agregado correctamente';
  document.getElementById('msgForm').textContent = '';

  document.getElementById('titulo').value = '';
  document.getElementById('autor').value = '';
  document.getElementById('anio').value = '';
});

function editarLibro(i) {
  const libro = books[i];

  document.getElementById('titulo').value = libro.titulo;
  document.getElementById('autor').value = libro.autor;
  document.getElementById('anio').value = libro.anio;
  document.getElementById('estado').value = libro.estado;

  editIndex = i;

  document.getElementById('btnAgregar').style.display = 'none';
  document.getElementById('btnUpdate').style.display = 'inline-block';

  // Limpiar mensajes al entrar a editar
  document.getElementById('msgForm').textContent = '';
  document.getElementById('msgExito').textContent = '';
}

document.getElementById('btnUpdate').addEventListener('click', function () {
  let titulo = document.getElementById('titulo').value;
  let autor = document.getElementById('autor').value;
  let anio = document.getElementById('anio').value;
  let estado = document.getElementById('estado').value;

  if (titulo === '' || autor === '' || anio === '') {
    document.getElementById('msgForm').textContent =
      'Todos los campos son obligatorios';
    document.getElementById('msgExito').textContent = '';
    return;
  }

  books[editIndex] = { titulo, autor, anio, estado };
  saveToLocal();
  renderBooks();

  document.getElementById('btnAgregar').style.display = 'inline-block';
  document.getElementById('btnUpdate').style.display = 'none';

  document.getElementById('msgExito').textContent =
    'Libro actualizado correctamente';
  document.getElementById('msgForm').textContent = '';

  // Limpiar campos
  document.getElementById('titulo').value = '';
  document.getElementById('autor').value = '';
  document.getElementById('anio').value = '';
});

// Eliminar libro
function eliminarLibro(i) {
  if (confirm('¿Estás seguro de que deseas eliminar este libro?')) {
    books.splice(i, 1);
    saveToLocal();
    renderBooks();

    //
    document.getElementById('msgExito').textContent =
      'Libro eliminado correctamente';
    document.getElementById('msgForm').textContent = '';
  }
}

renderBooks();
