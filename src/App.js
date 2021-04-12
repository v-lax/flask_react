import React, {useState,useEffect} from "react";
import Header from "./components/Header";
import AddCustomer from "./components/AddCustomer";
import axios from "axios"

function App() {
  
  const [customers,setCustomers]=useState();

  useEffect(()=>{
    axios.get('/results')
         .then((results)=>{
            console.log(results.data)
            setCustomers(results)
        })
  },[])
  return (
    <div className="App">
      <Header/>
      <AddCustomer/>
    </div>
  );
}

export default App;
