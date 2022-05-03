import './style.css';
import { handleFileSelect } from './parsing';

function component() {
  const element = document.createElement('div');

  // Lodash, now imported by this script
  document.getElementById('file-select').addEventListener('change', handleFileSelect, false);
  element.classList.add('hello');

  return element;
}

document.body.appendChild(component());