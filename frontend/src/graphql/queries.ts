import { gql } from "@apollo/client";


export const GET_AVIS = gql`
    query GeAvis {
        avis {
          id
          title
          content
          createdAt
          user {
            id
            username
          }
        }
    }
`;
