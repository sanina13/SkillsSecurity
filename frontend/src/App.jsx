import FileUpload from './components/FileUpload';
import ScanResults from './components/ScanResults';
import { useState } from 'react';

function App() {
  const [results, setResults] = useState(null);

  return (
    <div>
      <h1>SkillSecurity</h1>
      <p>Upload a .md skill file to scan for prompt injection</p>
      <FileUpload onResults={setResults} />
      <ScanResults results={results} />
    </div>
  );
}

export default App;
