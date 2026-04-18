import { useState } from 'react';

function FileUpload({ onResults }) {
  const [file, setFile] = useState(null);

  async function handleScan() {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/scan', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      onResults(data);

      console.log(data);
    } catch (error) {
      console.log('Erro:', error);
    }
  }

  return (
    <div>
      <input
        type="file"
        accept=".md"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleScan}>Scan</button>
    </div>
  );
}

export default FileUpload;
