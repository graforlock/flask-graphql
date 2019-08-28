import ApolloClient, { gql } from 'apollo-boost';

const client = new ApolloClient({
  uri: 'http://localhost:5000/graphql',
});

client
  .query({
    query: gql`
      {
        emails {
          edges {
            node {
              eid,
              subject,
              content
            }
          }
        }
      }`
  })
  .then(result => console.log(result));
