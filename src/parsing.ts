export function handleFileSelect(evt: Event) {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    const element = evt.currentTarget as HTMLInputElement;
    const files = element.files;
    const f = files[0]; 
    const reader = new FileReader();
    reader.onload = (function (thefile) {
      return function (e) {
        document.getElementById('file-contents').innerHTML = e.target.result as string;
      }
    })(f);
    reader.readAsText(f);
  }
}
