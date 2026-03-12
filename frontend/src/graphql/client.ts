import { ApolloClient, InMemoryCache, createHttpLink } from "@apollo/client";
import { setContext } from "@apollo/client/link/context";
import { ACCESS_TOKEN } from "../constant";

const httpLink = createHttpLink({
   uri: "http://localhost:8000/graphql/",
});


const authLink = setContext((_, { headers }) => {
	const token = localStorage.getItem(ACCESS_TOKEN);
	return {
	headers: { ...headers, authorization: token ? `${token}` : "",}
  };
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
})

export default client;
