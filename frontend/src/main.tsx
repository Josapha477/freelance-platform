import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { BrowserRouter } from 'react-router-dom';
import client from './graphql/client.ts';
import { ApolloProvider } from "@apollo/client/react"

createRoot(document.getElementById('root')!).render(
  <ApolloProvider client={client}>
  <BrowserRouter>
  <StrictMode>
    <App />
  </StrictMode>
    </BrowserRouter>
  </ApolloProvider>
)
