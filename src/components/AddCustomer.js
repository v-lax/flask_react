import React, { useState } from "react";
import Modal from "react-bootstrap/Modal";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/button';
import Col from 'react-bootstrap/Col';
import axios from "axios";


function AddCustomer() {
  const [isOpen, setIsOpen] = useState(false);

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const[email, setEmail]= useState("");
  const[phone, setPhone] = useState("");
  const[address,setAddress]= useState("");
  const[city,setCity]=useState("");
  const[state,setState] = useState("");
  const[zip, setZip] = useState("");

  const formData = {
    firstName:firstName,
    lastName:lastName,
    email:email,
    phone:phone,
    address:address,
    city:city,
    state:state,
    zip:zip
  }

  const showModal = () => {
    setIsOpen(true);
  };

  const hideModal = () => {
    setIsOpen(false);
    setFirstName("")
    setLastName("")
    setEmail("")
    setPhone("")
    setAddress("")
    setCity("")
    setState("")
    setZip("")
  };

  const handleSubmit = (event) =>{
      event.preventDefault()
      
      axios.post('/add', formData)
      .then((result) => {
        //access the results here....
        console.log(result)
      });
  }

  const firstNameChange = event => {
    const { value } = event.target;
    setFirstName(value);
  };

  const lastNameChange = event => {
    const { value } = event.target;
    setLastName(value);
  };

  const emailChange = event =>{
    const { value } = event.target;
    setEmail(value);
  }

  const phoneChange = event =>{
    const { value } = event.target;
    setPhone(value);
  }

  const addressChange = event =>{
    const {value} = event.target;
    setAddress(value)
  }

  const cityChange = event =>{
    const { value } = event.target
    setCity(value)
  }
  
  const stateChange = event =>{
    const {value} = event.target
    setState(value)
  }

  const zipChange = event =>{
    const {value} = event.target
    setZip(value)
  }

  return (
    <div className="navbar navbar-dark bg-dark justify-content-center">
      <button onClick={showModal}>Add Customer</button>
      <Modal show={isOpen} onHide={hideModal}>
        <Modal.Header closeButton>
          <Modal.Title>Add a Customer</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Row>
              <Form.Group as={Col} controlId="formGridEmail">
                <Form.Label>First Name</Form.Label>
                <Form.Control type="firstname" 
                              placeholder="first name" 
                              value={firstName}
                              onChange={firstNameChange} 
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="lastname" 
                              placeholder="last name"
                              value={lastName}
                              onChange={lastNameChange} 
                              />
              </Form.Group>
            </Form.Row>

            <Form.Group controlId="formGridAddress1">
              <Form.Label>email address</Form.Label>
              <Form.Control type="email" 
                            placeholder="name@example.com"
                            value={email}
                            onChange={emailChange}/>
            </Form.Group>

            <Form.Group controlId="formGridAddress2">
              <Form.Label>phone number</Form.Label>
              <Form.Control type="phone"
                            placeholder="phone number"
                            value={phone}
                            onChange={phoneChange}/>
            </Form.Group>

            <Form.Group controlId="formGridAddress2">
              <Form.Label>Address</Form.Label>
              <Form.Control type="address"
                            placeholder="Address"
                            value={address}
                            onChange={addressChange} />
            </Form.Group>

            <Form.Row>
              <Form.Group as={Col} controlId="formGridCity">
                <Form.Label>City</Form.Label>
                <Form.Control type="city"
                              placeholder="City Name"
                              value = {city}
                              onChange = {cityChange} />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>State</Form.Label>
                <Form.Control as="select" 
                              type="state"
                              defaultValue="Choose..."
                              value={state}
                              onChange = {stateChange}
                  >
                  <option value="AL">Choose...</option>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="DC">District Of Columbia</option>
                  <option value="FL">Florida</option>
                  <option value="GA">Georgia</option>
                  <option value="HI">Hawaii</option>
                  <option value="ID">Idaho</option>
                  <option value="IL">Illinois</option>
                  <option value="IN">Indiana</option>
                  <option value="IA">Iowa</option>
                  <option value="KS">Kansas</option>
                  <option value="KY">Kentucky</option>
                  <option value="LA">Louisiana</option>
                  <option value="ME">Maine</option>
                  <option value="MD">Maryland</option>
                  <option value="MA">Massachusetts</option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">New Hampshire</option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">North Carolina</option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">South Carolina</option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">West Virginia</option>
                  <option value="WI">Wisconsin</option>
                  <option value="WY">Wyoming</option>
                </Form.Control>
              </Form.Group>

              <Form.Group as={Col} controlId="formGridZip">
                <Form.Label>Zip</Form.Label>
                <Form.Control type="zip"
                              placeholder="Zip Code"
                              value = {zip}
                              onChange = {zipChange}
                
                />
              </Form.Group>
            </Form.Row>
            <Button type="submit">Submit form</Button>
          </Form>
        </Modal.Body>

      </Modal>
    </div>
  );
}

export default AddCustomer;