import React, { useCallback } from "react";
import "./App.css";
import { useDropzone } from "react-dropzone";

const getAccessToken = require("../services/api/getAccessToken").getAccessToken;
const submitJob = require("../services/api/submitJob").submitJob;

function MyDropzone() {
  const onDrop = useCallback(async acceptedFiles => {
    console.log('files', acceptedFiles) 
    const accessToken = await getAccessToken()
      .then(accessToken => {
        console.log('accessToken', accessToken);
      })
      .catch(error => {
        console.log(error);
      });
      submitJob(accessToken, acceptedFiles[0]);
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
          onClick={async () => {
            const accessToken = await getAccessToken()
              .then(accessToken => {
                console.log('accessToken', accessToken);
              })
              .catch(error => {
                console.log(error);
              });
              submitJob(accessToken, "./src/services/api/test.jpeg");
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
