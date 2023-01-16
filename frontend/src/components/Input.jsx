import React, {useEffect, useState} from 'react'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Messages from './Messages'
import pck from '../../package.json'
import {makePostRequest} from "../api-actions.js";
import {api} from "../api.js";
function Input() {
    const [apiVersion, setApiVersion] = useState('0')
    const [replica, setReplica] = useState('0')
    const [state, setState] = useState([])
    const [isSent, setSending] = useState(false)
    const [data, setData] = useState({"message_id":"",
        "message": "",
        "author": ""})

    const dataPreparing = (data) => {
        let messages = data["messages"];
        let arr = []
        const response = fetch(`${api}/api/info`, {
            method: 'GET',
            headers: {'Accept': 'application/json',}
        })  .then((response) => response.json())
            .then((json) =>{
                console.log(json);
                setApiVersion(json["backend_version"]);
                setReplica(json["replica_id"]);
            })

        for (let msg of messages) {
            arr.push(
                <Messages name={msg["author"]} message={msg["message"]}/>
            )
        }
        return arr
    }
    useEffect(() => {fetch(`${api}/api/messages`,
        {method: 'GET', headers: {'Accept': 'application/json',}}).then(response => {
        if (response.status === 200 || response.status === 201) {
            return response;
        }
        throw new Error();
    }).then(response => response.json()).then(data => {setState(dataPreparing(data))});
    }, [isSent])

    return (
        <>
            <div className='fixed bottom-0 left-0'>
                <div>{`Backend version: ${apiVersion}`}</div>
                <div>{`Frontend version: ${pck.version}`}</div>
                <div>{`Replica: ${replica}`}</div>
            </div>

        <div>
            <div className='flex flex-col  items-center justify-center my-10 space-y-3 p-3'>
                <TextField
                    label="Guest name"
                    size='small'
                    onChange={(evt) => {setData({...data, author: evt.target.value})}}
                />
                <TextField
                    label="Message"
                    size='small'
                    onChange={(evt) => {setData({...data, message: evt.target.value})}}
                />
                <Button
                    variant="contained"
                    onClick={(evt) => {
                        evt.preventDefault();
                        makePostRequest(data, setSending, isSent);
                    }
                    }
                >
                    Sign
                </Button>
            </div>
            <ul className='flex flex-col items-center justify-center my-10 space-y-3 p-3'>
                {state.map(x => x)}
            </ul>
        </div>
        </>
    )
}

export default Input