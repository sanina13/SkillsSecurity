function ScanResults({ results }) {
  if (!results) return null;

  return (
    <div>
      <h2>Results for {results.filename}</h2>
      <p>Total Findings: {results.total_findings}</p>
      {results.findings.map((finding, index) => (
        <div key={index}>
          <p>Rule: {finding.rule}</p>
          <p>Severity: {finding.severity}</p>
          <p>Line: {finding.line}</p>
          <p>Matched text: {finding.matched_text}</p>
        </div>
      ))}
    </div>
  );
}

export default ScanResults;
