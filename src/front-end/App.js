import React, { useCallback } from "react";
import "./App.css";
import { useDropzone } from "react-dropzone";

const getAccessToken = require("../services/api/getAccessToken").getAccessToken;
const submitJob = require("../services/api/submitJob").submitJob;

function MyDropzone() {
  const onDrop = useCallback(acceptedFiles => {
    const accessToken = getAccessToken()
      .then(accessToken => {
        submitJob(accessToken, acceptedFiles[0]);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Drop the files here ...</p>
      ) : (
        <p>Drag 'n' drop some files here, or click to select files</p>
      )}
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <button
          onClick={() => {
            const accessToken = getAccessToken()
              .then(response => {
                submitJob(response, "./src/services/api/test.jpeg");
              })
              .catch(error => {
                console.log(error);
              });
          }}
        >
          SEND REQUEST
        </button>
        <MyDropzone />
      </header>
    </div>
  );
}

export default App;
