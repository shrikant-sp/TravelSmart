# Generated TypeScript README
This README will guide you through the process of using the generated JavaScript SDK package for the connector `example`. It will also provide examples on how to use your generated SDK to call your Data Connect queries and mutations.

**If you're looking for the `React README`, you can find it at [`dataconnect-generated/react/README.md`](./react/README.md)**

***NOTE:** This README is generated alongside the generated SDK. If you make changes to this file, they will be overwritten when the SDK is regenerated.*

# Table of Contents
- [**Overview**](#generated-javascript-readme)
- [**Accessing the connector**](#accessing-the-connector)
  - [*Connecting to the local Emulator*](#connecting-to-the-local-emulator)
- [**Queries**](#queries)
  - [*GetUser*](#getuser)
  - [*ListUsers*](#listusers)
  - [*GetTrip*](#gettrip)
  - [*ListMyTrips*](#listmytrips)
  - [*GetBooking*](#getbooking)
  - [*ListBookings*](#listbookings)
  - [*GetActivity*](#getactivity)
  - [*ListActivities*](#listactivities)
  - [*GetExpense*](#getexpense)
  - [*ListExpenses*](#listexpenses)
  - [*GetTripMember*](#gettripmember)
  - [*ListTripMembers*](#listtripmembers)
- [**Mutations**](#mutations)
  - [*CreateUser*](#createuser)
  - [*UpdateUser*](#updateuser)
  - [*DeleteUser*](#deleteuser)
  - [*CreateTrip*](#createtrip)
  - [*UpdateTrip*](#updatetrip)
  - [*DeleteTrip*](#deletetrip)
  - [*CreateBooking*](#createbooking)
  - [*UpdateBooking*](#updatebooking)
  - [*DeleteBooking*](#deletebooking)
  - [*CreateActivity*](#createactivity)
  - [*UpdateActivity*](#updateactivity)
  - [*DeleteActivity*](#deleteactivity)
  - [*CreateExpense*](#createexpense)
  - [*UpdateExpense*](#updateexpense)
  - [*DeleteExpense*](#deleteexpense)
  - [*CreateTripMember*](#createtripmember)
  - [*UpdateTripMember*](#updatetripmember)
  - [*DeleteTripMember*](#deletetripmember)

# Accessing the connector
A connector is a collection of Queries and Mutations. One SDK is generated for each connector - this SDK is generated for the connector `example`. You can find more information about connectors in the [Data Connect documentation](https://firebase.google.com/docs/data-connect#how-does).

You can use this generated SDK by importing from the package `@dataconnect/generated` as shown below. Both CommonJS and ESM imports are supported.

You can also follow the instructions from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#set-client).

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig } from '@dataconnect/generated';

const dataConnect = getDataConnect(connectorConfig);
```

## Connecting to the local Emulator
By default, the connector will connect to the production service.

To connect to the emulator, you can use the following code.
You can also follow the emulator instructions from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#instrument-clients).

```typescript
import { connectDataConnectEmulator, getDataConnect } from 'firebase/data-connect';
import { connectorConfig } from '@dataconnect/generated';

const dataConnect = getDataConnect(connectorConfig);
connectDataConnectEmulator(dataConnect, 'localhost', 9399);
```

After it's initialized, you can call your Data Connect [queries](#queries) and [mutations](#mutations) from your generated SDK.

# Queries

There are two ways to execute a Data Connect Query using the generated Web SDK:
- Using a Query Reference function, which returns a `QueryRef`
  - The `QueryRef` can be used as an argument to `executeQuery()`, which will execute the Query and return a `QueryPromise`
- Using an action shortcut function, which returns a `QueryPromise`
  - Calling the action shortcut function will execute the Query and return a `QueryPromise`

The following is true for both the action shortcut function and the `QueryRef` function:
- The `QueryPromise` returned will resolve to the result of the Query once it has finished executing
- If the Query accepts arguments, both the action shortcut function and the `QueryRef` function accept a single argument: an object that contains all the required variables (and the optional variables) for the Query
- Both functions can be called with or without passing in a `DataConnect` instance as an argument. If no `DataConnect` argument is passed in, then the generated SDK will call `getDataConnect(connectorConfig)` behind the scenes for you.

Below are examples of how to use the `example` connector's generated functions to execute each query. You can also follow the examples from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#using-queries).

## GetUser
You can execute the `GetUser` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getUser(options?: ExecuteQueryOptions): QueryPromise<GetUserData, undefined>;

interface GetUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetUserData, undefined>;
}
export const getUserRef: GetUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getUser(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetUserData, undefined>;

interface GetUserRef {
  ...
  (dc: DataConnect): QueryRef<GetUserData, undefined>;
}
export const getUserRef: GetUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getUserRef:
```typescript
const name = getUserRef.operationName;
console.log(name);
```

### Variables
The `GetUser` query has no variables.
### Return Type
Recall that executing the `GetUser` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetUserData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetUserData {
  user?: {
    email: string;
    username: string;
  };
}
```
### Using `GetUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getUser } from '@dataconnect/generated';


// Call the `getUser()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getUser();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getUser(dataConnect);

console.log(data.user);

// Or, you can use the `Promise` API.
getUser().then((response) => {
  const data = response.data;
  console.log(data.user);
});
```

### Using `GetUser`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getUserRef } from '@dataconnect/generated';


// Call the `getUserRef()` function to get a reference to the query.
const ref = getUserRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getUserRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.user);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.user);
});
```

## ListUsers
You can execute the `ListUsers` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listUsers(options?: ExecuteQueryOptions): QueryPromise<ListUsersData, undefined>;

interface ListUsersRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListUsersData, undefined>;
}
export const listUsersRef: ListUsersRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listUsers(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListUsersData, undefined>;

interface ListUsersRef {
  ...
  (dc: DataConnect): QueryRef<ListUsersData, undefined>;
}
export const listUsersRef: ListUsersRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listUsersRef:
```typescript
const name = listUsersRef.operationName;
console.log(name);
```

### Variables
The `ListUsers` query has no variables.
### Return Type
Recall that executing the `ListUsers` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListUsersData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListUsersData {
  users: ({
    username: string;
  })[];
}
```
### Using `ListUsers`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listUsers } from '@dataconnect/generated';


// Call the `listUsers()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listUsers();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listUsers(dataConnect);

console.log(data.users);

// Or, you can use the `Promise` API.
listUsers().then((response) => {
  const data = response.data;
  console.log(data.users);
});
```

### Using `ListUsers`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listUsersRef } from '@dataconnect/generated';


// Call the `listUsersRef()` function to get a reference to the query.
const ref = listUsersRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listUsersRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.users);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.users);
});
```

## GetTrip
You can execute the `GetTrip` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getTrip(options?: ExecuteQueryOptions): QueryPromise<GetTripData, undefined>;

interface GetTripRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetTripData, undefined>;
}
export const getTripRef: GetTripRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getTrip(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetTripData, undefined>;

interface GetTripRef {
  ...
  (dc: DataConnect): QueryRef<GetTripData, undefined>;
}
export const getTripRef: GetTripRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getTripRef:
```typescript
const name = getTripRef.operationName;
console.log(name);
```

### Variables
The `GetTrip` query has no variables.
### Return Type
Recall that executing the `GetTrip` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetTripData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetTripData {
  trip?: {
    title: string;
    owner: {
      username: string;
    };
  };
}
```
### Using `GetTrip`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getTrip } from '@dataconnect/generated';


// Call the `getTrip()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getTrip();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getTrip(dataConnect);

console.log(data.trip);

// Or, you can use the `Promise` API.
getTrip().then((response) => {
  const data = response.data;
  console.log(data.trip);
});
```

### Using `GetTrip`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getTripRef } from '@dataconnect/generated';


// Call the `getTripRef()` function to get a reference to the query.
const ref = getTripRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getTripRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.trip);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.trip);
});
```

## ListMyTrips
You can execute the `ListMyTrips` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listMyTrips(options?: ExecuteQueryOptions): QueryPromise<ListMyTripsData, undefined>;

interface ListMyTripsRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListMyTripsData, undefined>;
}
export const listMyTripsRef: ListMyTripsRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listMyTrips(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListMyTripsData, undefined>;

interface ListMyTripsRef {
  ...
  (dc: DataConnect): QueryRef<ListMyTripsData, undefined>;
}
export const listMyTripsRef: ListMyTripsRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listMyTripsRef:
```typescript
const name = listMyTripsRef.operationName;
console.log(name);
```

### Variables
The `ListMyTrips` query has no variables.
### Return Type
Recall that executing the `ListMyTrips` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListMyTripsData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListMyTripsData {
  trips: ({
    title: string;
  })[];
}
```
### Using `ListMyTrips`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listMyTrips } from '@dataconnect/generated';


// Call the `listMyTrips()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listMyTrips();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listMyTrips(dataConnect);

console.log(data.trips);

// Or, you can use the `Promise` API.
listMyTrips().then((response) => {
  const data = response.data;
  console.log(data.trips);
});
```

### Using `ListMyTrips`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listMyTripsRef } from '@dataconnect/generated';


// Call the `listMyTripsRef()` function to get a reference to the query.
const ref = listMyTripsRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listMyTripsRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.trips);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.trips);
});
```

## GetBooking
You can execute the `GetBooking` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getBooking(options?: ExecuteQueryOptions): QueryPromise<GetBookingData, undefined>;

interface GetBookingRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetBookingData, undefined>;
}
export const getBookingRef: GetBookingRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getBooking(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetBookingData, undefined>;

interface GetBookingRef {
  ...
  (dc: DataConnect): QueryRef<GetBookingData, undefined>;
}
export const getBookingRef: GetBookingRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getBookingRef:
```typescript
const name = getBookingRef.operationName;
console.log(name);
```

### Variables
The `GetBooking` query has no variables.
### Return Type
Recall that executing the `GetBooking` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetBookingData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetBookingData {
  booking?: {
    providerName: string;
    cost?: number | null;
  };
}
```
### Using `GetBooking`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getBooking } from '@dataconnect/generated';


// Call the `getBooking()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getBooking();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getBooking(dataConnect);

console.log(data.booking);

// Or, you can use the `Promise` API.
getBooking().then((response) => {
  const data = response.data;
  console.log(data.booking);
});
```

### Using `GetBooking`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getBookingRef } from '@dataconnect/generated';


// Call the `getBookingRef()` function to get a reference to the query.
const ref = getBookingRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getBookingRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.booking);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.booking);
});
```

## ListBookings
You can execute the `ListBookings` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listBookings(options?: ExecuteQueryOptions): QueryPromise<ListBookingsData, undefined>;

interface ListBookingsRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListBookingsData, undefined>;
}
export const listBookingsRef: ListBookingsRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listBookings(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListBookingsData, undefined>;

interface ListBookingsRef {
  ...
  (dc: DataConnect): QueryRef<ListBookingsData, undefined>;
}
export const listBookingsRef: ListBookingsRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listBookingsRef:
```typescript
const name = listBookingsRef.operationName;
console.log(name);
```

### Variables
The `ListBookings` query has no variables.
### Return Type
Recall that executing the `ListBookings` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListBookingsData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListBookingsData {
  bookings: ({
    type: string;
    providerName: string;
  })[];
}
```
### Using `ListBookings`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listBookings } from '@dataconnect/generated';


// Call the `listBookings()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listBookings();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listBookings(dataConnect);

console.log(data.bookings);

// Or, you can use the `Promise` API.
listBookings().then((response) => {
  const data = response.data;
  console.log(data.bookings);
});
```

### Using `ListBookings`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listBookingsRef } from '@dataconnect/generated';


// Call the `listBookingsRef()` function to get a reference to the query.
const ref = listBookingsRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listBookingsRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.bookings);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.bookings);
});
```

## GetActivity
You can execute the `GetActivity` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getActivity(options?: ExecuteQueryOptions): QueryPromise<GetActivityData, undefined>;

interface GetActivityRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetActivityData, undefined>;
}
export const getActivityRef: GetActivityRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getActivity(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetActivityData, undefined>;

interface GetActivityRef {
  ...
  (dc: DataConnect): QueryRef<GetActivityData, undefined>;
}
export const getActivityRef: GetActivityRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getActivityRef:
```typescript
const name = getActivityRef.operationName;
console.log(name);
```

### Variables
The `GetActivity` query has no variables.
### Return Type
Recall that executing the `GetActivity` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetActivityData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetActivityData {
  activity?: {
    title: string;
    startTime: TimestampString;
  };
}
```
### Using `GetActivity`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getActivity } from '@dataconnect/generated';


// Call the `getActivity()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getActivity();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getActivity(dataConnect);

console.log(data.activity);

// Or, you can use the `Promise` API.
getActivity().then((response) => {
  const data = response.data;
  console.log(data.activity);
});
```

### Using `GetActivity`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getActivityRef } from '@dataconnect/generated';


// Call the `getActivityRef()` function to get a reference to the query.
const ref = getActivityRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getActivityRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.activity);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.activity);
});
```

## ListActivities
You can execute the `ListActivities` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listActivities(options?: ExecuteQueryOptions): QueryPromise<ListActivitiesData, undefined>;

interface ListActivitiesRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListActivitiesData, undefined>;
}
export const listActivitiesRef: ListActivitiesRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listActivities(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListActivitiesData, undefined>;

interface ListActivitiesRef {
  ...
  (dc: DataConnect): QueryRef<ListActivitiesData, undefined>;
}
export const listActivitiesRef: ListActivitiesRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listActivitiesRef:
```typescript
const name = listActivitiesRef.operationName;
console.log(name);
```

### Variables
The `ListActivities` query has no variables.
### Return Type
Recall that executing the `ListActivities` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListActivitiesData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListActivitiesData {
  activities: ({
    title: string;
    locationName?: string | null;
  })[];
}
```
### Using `ListActivities`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listActivities } from '@dataconnect/generated';


// Call the `listActivities()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listActivities();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listActivities(dataConnect);

console.log(data.activities);

// Or, you can use the `Promise` API.
listActivities().then((response) => {
  const data = response.data;
  console.log(data.activities);
});
```

### Using `ListActivities`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listActivitiesRef } from '@dataconnect/generated';


// Call the `listActivitiesRef()` function to get a reference to the query.
const ref = listActivitiesRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listActivitiesRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.activities);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.activities);
});
```

## GetExpense
You can execute the `GetExpense` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getExpense(options?: ExecuteQueryOptions): QueryPromise<GetExpenseData, undefined>;

interface GetExpenseRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetExpenseData, undefined>;
}
export const getExpenseRef: GetExpenseRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getExpense(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetExpenseData, undefined>;

interface GetExpenseRef {
  ...
  (dc: DataConnect): QueryRef<GetExpenseData, undefined>;
}
export const getExpenseRef: GetExpenseRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getExpenseRef:
```typescript
const name = getExpenseRef.operationName;
console.log(name);
```

### Variables
The `GetExpense` query has no variables.
### Return Type
Recall that executing the `GetExpense` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetExpenseData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetExpenseData {
  expense?: {
    amount: number;
    category: string;
  };
}
```
### Using `GetExpense`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getExpense } from '@dataconnect/generated';


// Call the `getExpense()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getExpense();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getExpense(dataConnect);

console.log(data.expense);

// Or, you can use the `Promise` API.
getExpense().then((response) => {
  const data = response.data;
  console.log(data.expense);
});
```

### Using `GetExpense`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getExpenseRef } from '@dataconnect/generated';


// Call the `getExpenseRef()` function to get a reference to the query.
const ref = getExpenseRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getExpenseRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.expense);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.expense);
});
```

## ListExpenses
You can execute the `ListExpenses` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listExpenses(options?: ExecuteQueryOptions): QueryPromise<ListExpensesData, undefined>;

interface ListExpensesRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListExpensesData, undefined>;
}
export const listExpensesRef: ListExpensesRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listExpenses(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListExpensesData, undefined>;

interface ListExpensesRef {
  ...
  (dc: DataConnect): QueryRef<ListExpensesData, undefined>;
}
export const listExpensesRef: ListExpensesRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listExpensesRef:
```typescript
const name = listExpensesRef.operationName;
console.log(name);
```

### Variables
The `ListExpenses` query has no variables.
### Return Type
Recall that executing the `ListExpenses` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListExpensesData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListExpensesData {
  expenses: ({
    amount: number;
    category: string;
    payer?: {
      username: string;
    };
  })[];
}
```
### Using `ListExpenses`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listExpenses } from '@dataconnect/generated';


// Call the `listExpenses()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listExpenses();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listExpenses(dataConnect);

console.log(data.expenses);

// Or, you can use the `Promise` API.
listExpenses().then((response) => {
  const data = response.data;
  console.log(data.expenses);
});
```

### Using `ListExpenses`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listExpensesRef } from '@dataconnect/generated';


// Call the `listExpensesRef()` function to get a reference to the query.
const ref = listExpensesRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listExpensesRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.expenses);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.expenses);
});
```

## GetTripMember
You can execute the `GetTripMember` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
getTripMember(options?: ExecuteQueryOptions): QueryPromise<GetTripMemberData, undefined>;

interface GetTripMemberRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetTripMemberData, undefined>;
}
export const getTripMemberRef: GetTripMemberRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
getTripMember(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetTripMemberData, undefined>;

interface GetTripMemberRef {
  ...
  (dc: DataConnect): QueryRef<GetTripMemberData, undefined>;
}
export const getTripMemberRef: GetTripMemberRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the getTripMemberRef:
```typescript
const name = getTripMemberRef.operationName;
console.log(name);
```

### Variables
The `GetTripMember` query has no variables.
### Return Type
Recall that executing the `GetTripMember` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `GetTripMemberData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface GetTripMemberData {
  tripMember?: {
    role?: string | null;
    user: {
      username: string;
    };
  };
}
```
### Using `GetTripMember`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, getTripMember } from '@dataconnect/generated';


// Call the `getTripMember()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await getTripMember();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await getTripMember(dataConnect);

console.log(data.tripMember);

// Or, you can use the `Promise` API.
getTripMember().then((response) => {
  const data = response.data;
  console.log(data.tripMember);
});
```

### Using `GetTripMember`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, getTripMemberRef } from '@dataconnect/generated';


// Call the `getTripMemberRef()` function to get a reference to the query.
const ref = getTripMemberRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = getTripMemberRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.tripMember);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.tripMember);
});
```

## ListTripMembers
You can execute the `ListTripMembers` query using the following action shortcut function, or by calling `executeQuery()` after calling the following `QueryRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
listTripMembers(options?: ExecuteQueryOptions): QueryPromise<ListTripMembersData, undefined>;

interface ListTripMembersRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListTripMembersData, undefined>;
}
export const listTripMembersRef: ListTripMembersRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `QueryRef` function.
```typescript
listTripMembers(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListTripMembersData, undefined>;

interface ListTripMembersRef {
  ...
  (dc: DataConnect): QueryRef<ListTripMembersData, undefined>;
}
export const listTripMembersRef: ListTripMembersRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the listTripMembersRef:
```typescript
const name = listTripMembersRef.operationName;
console.log(name);
```

### Variables
The `ListTripMembers` query has no variables.
### Return Type
Recall that executing the `ListTripMembers` query returns a `QueryPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `ListTripMembersData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface ListTripMembersData {
  tripMembers: ({
    role?: string | null;
    user: {
      username: string;
    };
  })[];
}
```
### Using `ListTripMembers`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, listTripMembers } from '@dataconnect/generated';


// Call the `listTripMembers()` function to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await listTripMembers();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await listTripMembers(dataConnect);

console.log(data.tripMembers);

// Or, you can use the `Promise` API.
listTripMembers().then((response) => {
  const data = response.data;
  console.log(data.tripMembers);
});
```

### Using `ListTripMembers`'s `QueryRef` function

```typescript
import { getDataConnect, executeQuery } from 'firebase/data-connect';
import { connectorConfig, listTripMembersRef } from '@dataconnect/generated';


// Call the `listTripMembersRef()` function to get a reference to the query.
const ref = listTripMembersRef();

// You can also pass in a `DataConnect` instance to the `QueryRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = listTripMembersRef(dataConnect);

// Call `executeQuery()` on the reference to execute the query.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeQuery(ref);

console.log(data.tripMembers);

// Or, you can use the `Promise` API.
executeQuery(ref).then((response) => {
  const data = response.data;
  console.log(data.tripMembers);
});
```

# Mutations

There are two ways to execute a Data Connect Mutation using the generated Web SDK:
- Using a Mutation Reference function, which returns a `MutationRef`
  - The `MutationRef` can be used as an argument to `executeMutation()`, which will execute the Mutation and return a `MutationPromise`
- Using an action shortcut function, which returns a `MutationPromise`
  - Calling the action shortcut function will execute the Mutation and return a `MutationPromise`

The following is true for both the action shortcut function and the `MutationRef` function:
- The `MutationPromise` returned will resolve to the result of the Mutation once it has finished executing
- If the Mutation accepts arguments, both the action shortcut function and the `MutationRef` function accept a single argument: an object that contains all the required variables (and the optional variables) for the Mutation
- Both functions can be called with or without passing in a `DataConnect` instance as an argument. If no `DataConnect` argument is passed in, then the generated SDK will call `getDataConnect(connectorConfig)` behind the scenes for you.

Below are examples of how to use the `example` connector's generated functions to execute each mutation. You can also follow the examples from the [Data Connect documentation](https://firebase.google.com/docs/data-connect/web-sdk#using-mutations).

## CreateUser
You can execute the `CreateUser` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createUser(): MutationPromise<CreateUserData, undefined>;

interface CreateUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateUserData, undefined>;
}
export const createUserRef: CreateUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createUser(dc: DataConnect): MutationPromise<CreateUserData, undefined>;

interface CreateUserRef {
  ...
  (dc: DataConnect): MutationRef<CreateUserData, undefined>;
}
export const createUserRef: CreateUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createUserRef:
```typescript
const name = createUserRef.operationName;
console.log(name);
```

### Variables
The `CreateUser` mutation has no variables.
### Return Type
Recall that executing the `CreateUser` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateUserData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateUserData {
  user_insert: User_Key;
}
```
### Using `CreateUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createUser } from '@dataconnect/generated';


// Call the `createUser()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createUser();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createUser(dataConnect);

console.log(data.user_insert);

// Or, you can use the `Promise` API.
createUser().then((response) => {
  const data = response.data;
  console.log(data.user_insert);
});
```

### Using `CreateUser`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createUserRef } from '@dataconnect/generated';


// Call the `createUserRef()` function to get a reference to the mutation.
const ref = createUserRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createUserRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.user_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.user_insert);
});
```

## UpdateUser
You can execute the `UpdateUser` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateUser(): MutationPromise<UpdateUserData, undefined>;

interface UpdateUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateUserData, undefined>;
}
export const updateUserRef: UpdateUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateUser(dc: DataConnect): MutationPromise<UpdateUserData, undefined>;

interface UpdateUserRef {
  ...
  (dc: DataConnect): MutationRef<UpdateUserData, undefined>;
}
export const updateUserRef: UpdateUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateUserRef:
```typescript
const name = updateUserRef.operationName;
console.log(name);
```

### Variables
The `UpdateUser` mutation has no variables.
### Return Type
Recall that executing the `UpdateUser` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateUserData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateUserData {
  user_update?: User_Key | null;
}
```
### Using `UpdateUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateUser } from '@dataconnect/generated';


// Call the `updateUser()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateUser();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateUser(dataConnect);

console.log(data.user_update);

// Or, you can use the `Promise` API.
updateUser().then((response) => {
  const data = response.data;
  console.log(data.user_update);
});
```

### Using `UpdateUser`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateUserRef } from '@dataconnect/generated';


// Call the `updateUserRef()` function to get a reference to the mutation.
const ref = updateUserRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateUserRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.user_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.user_update);
});
```

## DeleteUser
You can execute the `DeleteUser` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteUser(): MutationPromise<DeleteUserData, undefined>;

interface DeleteUserRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteUserData, undefined>;
}
export const deleteUserRef: DeleteUserRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteUser(dc: DataConnect): MutationPromise<DeleteUserData, undefined>;

interface DeleteUserRef {
  ...
  (dc: DataConnect): MutationRef<DeleteUserData, undefined>;
}
export const deleteUserRef: DeleteUserRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteUserRef:
```typescript
const name = deleteUserRef.operationName;
console.log(name);
```

### Variables
The `DeleteUser` mutation has no variables.
### Return Type
Recall that executing the `DeleteUser` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteUserData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteUserData {
  user_delete?: User_Key | null;
}
```
### Using `DeleteUser`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteUser } from '@dataconnect/generated';


// Call the `deleteUser()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteUser();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteUser(dataConnect);

console.log(data.user_delete);

// Or, you can use the `Promise` API.
deleteUser().then((response) => {
  const data = response.data;
  console.log(data.user_delete);
});
```

### Using `DeleteUser`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteUserRef } from '@dataconnect/generated';


// Call the `deleteUserRef()` function to get a reference to the mutation.
const ref = deleteUserRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteUserRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.user_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.user_delete);
});
```

## CreateTrip
You can execute the `CreateTrip` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createTrip(): MutationPromise<CreateTripData, undefined>;

interface CreateTripRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateTripData, undefined>;
}
export const createTripRef: CreateTripRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createTrip(dc: DataConnect): MutationPromise<CreateTripData, undefined>;

interface CreateTripRef {
  ...
  (dc: DataConnect): MutationRef<CreateTripData, undefined>;
}
export const createTripRef: CreateTripRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createTripRef:
```typescript
const name = createTripRef.operationName;
console.log(name);
```

### Variables
The `CreateTrip` mutation has no variables.
### Return Type
Recall that executing the `CreateTrip` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateTripData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateTripData {
  trip_insert: Trip_Key;
}
```
### Using `CreateTrip`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createTrip } from '@dataconnect/generated';


// Call the `createTrip()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createTrip();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createTrip(dataConnect);

console.log(data.trip_insert);

// Or, you can use the `Promise` API.
createTrip().then((response) => {
  const data = response.data;
  console.log(data.trip_insert);
});
```

### Using `CreateTrip`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createTripRef } from '@dataconnect/generated';


// Call the `createTripRef()` function to get a reference to the mutation.
const ref = createTripRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createTripRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.trip_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.trip_insert);
});
```

## UpdateTrip
You can execute the `UpdateTrip` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateTrip(): MutationPromise<UpdateTripData, undefined>;

interface UpdateTripRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateTripData, undefined>;
}
export const updateTripRef: UpdateTripRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateTrip(dc: DataConnect): MutationPromise<UpdateTripData, undefined>;

interface UpdateTripRef {
  ...
  (dc: DataConnect): MutationRef<UpdateTripData, undefined>;
}
export const updateTripRef: UpdateTripRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateTripRef:
```typescript
const name = updateTripRef.operationName;
console.log(name);
```

### Variables
The `UpdateTrip` mutation has no variables.
### Return Type
Recall that executing the `UpdateTrip` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateTripData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateTripData {
  trip_update?: Trip_Key | null;
}
```
### Using `UpdateTrip`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateTrip } from '@dataconnect/generated';


// Call the `updateTrip()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateTrip();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateTrip(dataConnect);

console.log(data.trip_update);

// Or, you can use the `Promise` API.
updateTrip().then((response) => {
  const data = response.data;
  console.log(data.trip_update);
});
```

### Using `UpdateTrip`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateTripRef } from '@dataconnect/generated';


// Call the `updateTripRef()` function to get a reference to the mutation.
const ref = updateTripRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateTripRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.trip_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.trip_update);
});
```

## DeleteTrip
You can execute the `DeleteTrip` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteTrip(): MutationPromise<DeleteTripData, undefined>;

interface DeleteTripRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteTripData, undefined>;
}
export const deleteTripRef: DeleteTripRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteTrip(dc: DataConnect): MutationPromise<DeleteTripData, undefined>;

interface DeleteTripRef {
  ...
  (dc: DataConnect): MutationRef<DeleteTripData, undefined>;
}
export const deleteTripRef: DeleteTripRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteTripRef:
```typescript
const name = deleteTripRef.operationName;
console.log(name);
```

### Variables
The `DeleteTrip` mutation has no variables.
### Return Type
Recall that executing the `DeleteTrip` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteTripData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteTripData {
  trip_delete?: Trip_Key | null;
}
```
### Using `DeleteTrip`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteTrip } from '@dataconnect/generated';


// Call the `deleteTrip()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteTrip();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteTrip(dataConnect);

console.log(data.trip_delete);

// Or, you can use the `Promise` API.
deleteTrip().then((response) => {
  const data = response.data;
  console.log(data.trip_delete);
});
```

### Using `DeleteTrip`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteTripRef } from '@dataconnect/generated';


// Call the `deleteTripRef()` function to get a reference to the mutation.
const ref = deleteTripRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteTripRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.trip_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.trip_delete);
});
```

## CreateBooking
You can execute the `CreateBooking` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createBooking(): MutationPromise<CreateBookingData, undefined>;

interface CreateBookingRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateBookingData, undefined>;
}
export const createBookingRef: CreateBookingRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createBooking(dc: DataConnect): MutationPromise<CreateBookingData, undefined>;

interface CreateBookingRef {
  ...
  (dc: DataConnect): MutationRef<CreateBookingData, undefined>;
}
export const createBookingRef: CreateBookingRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createBookingRef:
```typescript
const name = createBookingRef.operationName;
console.log(name);
```

### Variables
The `CreateBooking` mutation has no variables.
### Return Type
Recall that executing the `CreateBooking` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateBookingData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateBookingData {
  booking_insert: Booking_Key;
}
```
### Using `CreateBooking`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createBooking } from '@dataconnect/generated';


// Call the `createBooking()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createBooking();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createBooking(dataConnect);

console.log(data.booking_insert);

// Or, you can use the `Promise` API.
createBooking().then((response) => {
  const data = response.data;
  console.log(data.booking_insert);
});
```

### Using `CreateBooking`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createBookingRef } from '@dataconnect/generated';


// Call the `createBookingRef()` function to get a reference to the mutation.
const ref = createBookingRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createBookingRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.booking_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.booking_insert);
});
```

## UpdateBooking
You can execute the `UpdateBooking` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateBooking(): MutationPromise<UpdateBookingData, undefined>;

interface UpdateBookingRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateBookingData, undefined>;
}
export const updateBookingRef: UpdateBookingRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateBooking(dc: DataConnect): MutationPromise<UpdateBookingData, undefined>;

interface UpdateBookingRef {
  ...
  (dc: DataConnect): MutationRef<UpdateBookingData, undefined>;
}
export const updateBookingRef: UpdateBookingRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateBookingRef:
```typescript
const name = updateBookingRef.operationName;
console.log(name);
```

### Variables
The `UpdateBooking` mutation has no variables.
### Return Type
Recall that executing the `UpdateBooking` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateBookingData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateBookingData {
  booking_update?: Booking_Key | null;
}
```
### Using `UpdateBooking`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateBooking } from '@dataconnect/generated';


// Call the `updateBooking()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateBooking();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateBooking(dataConnect);

console.log(data.booking_update);

// Or, you can use the `Promise` API.
updateBooking().then((response) => {
  const data = response.data;
  console.log(data.booking_update);
});
```

### Using `UpdateBooking`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateBookingRef } from '@dataconnect/generated';


// Call the `updateBookingRef()` function to get a reference to the mutation.
const ref = updateBookingRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateBookingRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.booking_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.booking_update);
});
```

## DeleteBooking
You can execute the `DeleteBooking` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteBooking(): MutationPromise<DeleteBookingData, undefined>;

interface DeleteBookingRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteBookingData, undefined>;
}
export const deleteBookingRef: DeleteBookingRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteBooking(dc: DataConnect): MutationPromise<DeleteBookingData, undefined>;

interface DeleteBookingRef {
  ...
  (dc: DataConnect): MutationRef<DeleteBookingData, undefined>;
}
export const deleteBookingRef: DeleteBookingRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteBookingRef:
```typescript
const name = deleteBookingRef.operationName;
console.log(name);
```

### Variables
The `DeleteBooking` mutation has no variables.
### Return Type
Recall that executing the `DeleteBooking` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteBookingData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteBookingData {
  booking_delete?: Booking_Key | null;
}
```
### Using `DeleteBooking`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteBooking } from '@dataconnect/generated';


// Call the `deleteBooking()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteBooking();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteBooking(dataConnect);

console.log(data.booking_delete);

// Or, you can use the `Promise` API.
deleteBooking().then((response) => {
  const data = response.data;
  console.log(data.booking_delete);
});
```

### Using `DeleteBooking`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteBookingRef } from '@dataconnect/generated';


// Call the `deleteBookingRef()` function to get a reference to the mutation.
const ref = deleteBookingRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteBookingRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.booking_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.booking_delete);
});
```

## CreateActivity
You can execute the `CreateActivity` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createActivity(): MutationPromise<CreateActivityData, undefined>;

interface CreateActivityRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateActivityData, undefined>;
}
export const createActivityRef: CreateActivityRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createActivity(dc: DataConnect): MutationPromise<CreateActivityData, undefined>;

interface CreateActivityRef {
  ...
  (dc: DataConnect): MutationRef<CreateActivityData, undefined>;
}
export const createActivityRef: CreateActivityRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createActivityRef:
```typescript
const name = createActivityRef.operationName;
console.log(name);
```

### Variables
The `CreateActivity` mutation has no variables.
### Return Type
Recall that executing the `CreateActivity` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateActivityData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateActivityData {
  activity_insert: Activity_Key;
}
```
### Using `CreateActivity`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createActivity } from '@dataconnect/generated';


// Call the `createActivity()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createActivity();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createActivity(dataConnect);

console.log(data.activity_insert);

// Or, you can use the `Promise` API.
createActivity().then((response) => {
  const data = response.data;
  console.log(data.activity_insert);
});
```

### Using `CreateActivity`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createActivityRef } from '@dataconnect/generated';


// Call the `createActivityRef()` function to get a reference to the mutation.
const ref = createActivityRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createActivityRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.activity_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.activity_insert);
});
```

## UpdateActivity
You can execute the `UpdateActivity` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateActivity(): MutationPromise<UpdateActivityData, undefined>;

interface UpdateActivityRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateActivityData, undefined>;
}
export const updateActivityRef: UpdateActivityRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateActivity(dc: DataConnect): MutationPromise<UpdateActivityData, undefined>;

interface UpdateActivityRef {
  ...
  (dc: DataConnect): MutationRef<UpdateActivityData, undefined>;
}
export const updateActivityRef: UpdateActivityRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateActivityRef:
```typescript
const name = updateActivityRef.operationName;
console.log(name);
```

### Variables
The `UpdateActivity` mutation has no variables.
### Return Type
Recall that executing the `UpdateActivity` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateActivityData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateActivityData {
  activity_update?: Activity_Key | null;
}
```
### Using `UpdateActivity`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateActivity } from '@dataconnect/generated';


// Call the `updateActivity()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateActivity();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateActivity(dataConnect);

console.log(data.activity_update);

// Or, you can use the `Promise` API.
updateActivity().then((response) => {
  const data = response.data;
  console.log(data.activity_update);
});
```

### Using `UpdateActivity`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateActivityRef } from '@dataconnect/generated';


// Call the `updateActivityRef()` function to get a reference to the mutation.
const ref = updateActivityRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateActivityRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.activity_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.activity_update);
});
```

## DeleteActivity
You can execute the `DeleteActivity` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteActivity(): MutationPromise<DeleteActivityData, undefined>;

interface DeleteActivityRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteActivityData, undefined>;
}
export const deleteActivityRef: DeleteActivityRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteActivity(dc: DataConnect): MutationPromise<DeleteActivityData, undefined>;

interface DeleteActivityRef {
  ...
  (dc: DataConnect): MutationRef<DeleteActivityData, undefined>;
}
export const deleteActivityRef: DeleteActivityRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteActivityRef:
```typescript
const name = deleteActivityRef.operationName;
console.log(name);
```

### Variables
The `DeleteActivity` mutation has no variables.
### Return Type
Recall that executing the `DeleteActivity` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteActivityData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteActivityData {
  activity_delete?: Activity_Key | null;
}
```
### Using `DeleteActivity`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteActivity } from '@dataconnect/generated';


// Call the `deleteActivity()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteActivity();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteActivity(dataConnect);

console.log(data.activity_delete);

// Or, you can use the `Promise` API.
deleteActivity().then((response) => {
  const data = response.data;
  console.log(data.activity_delete);
});
```

### Using `DeleteActivity`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteActivityRef } from '@dataconnect/generated';


// Call the `deleteActivityRef()` function to get a reference to the mutation.
const ref = deleteActivityRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteActivityRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.activity_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.activity_delete);
});
```

## CreateExpense
You can execute the `CreateExpense` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createExpense(): MutationPromise<CreateExpenseData, undefined>;

interface CreateExpenseRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateExpenseData, undefined>;
}
export const createExpenseRef: CreateExpenseRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createExpense(dc: DataConnect): MutationPromise<CreateExpenseData, undefined>;

interface CreateExpenseRef {
  ...
  (dc: DataConnect): MutationRef<CreateExpenseData, undefined>;
}
export const createExpenseRef: CreateExpenseRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createExpenseRef:
```typescript
const name = createExpenseRef.operationName;
console.log(name);
```

### Variables
The `CreateExpense` mutation has no variables.
### Return Type
Recall that executing the `CreateExpense` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateExpenseData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateExpenseData {
  expense_insert: Expense_Key;
}
```
### Using `CreateExpense`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createExpense } from '@dataconnect/generated';


// Call the `createExpense()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createExpense();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createExpense(dataConnect);

console.log(data.expense_insert);

// Or, you can use the `Promise` API.
createExpense().then((response) => {
  const data = response.data;
  console.log(data.expense_insert);
});
```

### Using `CreateExpense`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createExpenseRef } from '@dataconnect/generated';


// Call the `createExpenseRef()` function to get a reference to the mutation.
const ref = createExpenseRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createExpenseRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.expense_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.expense_insert);
});
```

## UpdateExpense
You can execute the `UpdateExpense` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateExpense(): MutationPromise<UpdateExpenseData, undefined>;

interface UpdateExpenseRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateExpenseData, undefined>;
}
export const updateExpenseRef: UpdateExpenseRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateExpense(dc: DataConnect): MutationPromise<UpdateExpenseData, undefined>;

interface UpdateExpenseRef {
  ...
  (dc: DataConnect): MutationRef<UpdateExpenseData, undefined>;
}
export const updateExpenseRef: UpdateExpenseRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateExpenseRef:
```typescript
const name = updateExpenseRef.operationName;
console.log(name);
```

### Variables
The `UpdateExpense` mutation has no variables.
### Return Type
Recall that executing the `UpdateExpense` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateExpenseData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateExpenseData {
  expense_update?: Expense_Key | null;
}
```
### Using `UpdateExpense`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateExpense } from '@dataconnect/generated';


// Call the `updateExpense()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateExpense();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateExpense(dataConnect);

console.log(data.expense_update);

// Or, you can use the `Promise` API.
updateExpense().then((response) => {
  const data = response.data;
  console.log(data.expense_update);
});
```

### Using `UpdateExpense`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateExpenseRef } from '@dataconnect/generated';


// Call the `updateExpenseRef()` function to get a reference to the mutation.
const ref = updateExpenseRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateExpenseRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.expense_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.expense_update);
});
```

## DeleteExpense
You can execute the `DeleteExpense` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteExpense(): MutationPromise<DeleteExpenseData, undefined>;

interface DeleteExpenseRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteExpenseData, undefined>;
}
export const deleteExpenseRef: DeleteExpenseRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteExpense(dc: DataConnect): MutationPromise<DeleteExpenseData, undefined>;

interface DeleteExpenseRef {
  ...
  (dc: DataConnect): MutationRef<DeleteExpenseData, undefined>;
}
export const deleteExpenseRef: DeleteExpenseRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteExpenseRef:
```typescript
const name = deleteExpenseRef.operationName;
console.log(name);
```

### Variables
The `DeleteExpense` mutation has no variables.
### Return Type
Recall that executing the `DeleteExpense` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteExpenseData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteExpenseData {
  expense_delete?: Expense_Key | null;
}
```
### Using `DeleteExpense`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteExpense } from '@dataconnect/generated';


// Call the `deleteExpense()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteExpense();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteExpense(dataConnect);

console.log(data.expense_delete);

// Or, you can use the `Promise` API.
deleteExpense().then((response) => {
  const data = response.data;
  console.log(data.expense_delete);
});
```

### Using `DeleteExpense`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteExpenseRef } from '@dataconnect/generated';


// Call the `deleteExpenseRef()` function to get a reference to the mutation.
const ref = deleteExpenseRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteExpenseRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.expense_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.expense_delete);
});
```

## CreateTripMember
You can execute the `CreateTripMember` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
createTripMember(): MutationPromise<CreateTripMemberData, undefined>;

interface CreateTripMemberRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateTripMemberData, undefined>;
}
export const createTripMemberRef: CreateTripMemberRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
createTripMember(dc: DataConnect): MutationPromise<CreateTripMemberData, undefined>;

interface CreateTripMemberRef {
  ...
  (dc: DataConnect): MutationRef<CreateTripMemberData, undefined>;
}
export const createTripMemberRef: CreateTripMemberRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the createTripMemberRef:
```typescript
const name = createTripMemberRef.operationName;
console.log(name);
```

### Variables
The `CreateTripMember` mutation has no variables.
### Return Type
Recall that executing the `CreateTripMember` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `CreateTripMemberData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface CreateTripMemberData {
  tripMember_insert: TripMember_Key;
}
```
### Using `CreateTripMember`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, createTripMember } from '@dataconnect/generated';


// Call the `createTripMember()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await createTripMember();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await createTripMember(dataConnect);

console.log(data.tripMember_insert);

// Or, you can use the `Promise` API.
createTripMember().then((response) => {
  const data = response.data;
  console.log(data.tripMember_insert);
});
```

### Using `CreateTripMember`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, createTripMemberRef } from '@dataconnect/generated';


// Call the `createTripMemberRef()` function to get a reference to the mutation.
const ref = createTripMemberRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = createTripMemberRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.tripMember_insert);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.tripMember_insert);
});
```

## UpdateTripMember
You can execute the `UpdateTripMember` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
updateTripMember(): MutationPromise<UpdateTripMemberData, undefined>;

interface UpdateTripMemberRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateTripMemberData, undefined>;
}
export const updateTripMemberRef: UpdateTripMemberRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
updateTripMember(dc: DataConnect): MutationPromise<UpdateTripMemberData, undefined>;

interface UpdateTripMemberRef {
  ...
  (dc: DataConnect): MutationRef<UpdateTripMemberData, undefined>;
}
export const updateTripMemberRef: UpdateTripMemberRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the updateTripMemberRef:
```typescript
const name = updateTripMemberRef.operationName;
console.log(name);
```

### Variables
The `UpdateTripMember` mutation has no variables.
### Return Type
Recall that executing the `UpdateTripMember` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `UpdateTripMemberData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface UpdateTripMemberData {
  tripMember_update?: TripMember_Key | null;
}
```
### Using `UpdateTripMember`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, updateTripMember } from '@dataconnect/generated';


// Call the `updateTripMember()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await updateTripMember();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await updateTripMember(dataConnect);

console.log(data.tripMember_update);

// Or, you can use the `Promise` API.
updateTripMember().then((response) => {
  const data = response.data;
  console.log(data.tripMember_update);
});
```

### Using `UpdateTripMember`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, updateTripMemberRef } from '@dataconnect/generated';


// Call the `updateTripMemberRef()` function to get a reference to the mutation.
const ref = updateTripMemberRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = updateTripMemberRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.tripMember_update);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.tripMember_update);
});
```

## DeleteTripMember
You can execute the `DeleteTripMember` mutation using the following action shortcut function, or by calling `executeMutation()` after calling the following `MutationRef` function, both of which are defined in [dataconnect-generated/index.d.ts](./index.d.ts):
```typescript
deleteTripMember(): MutationPromise<DeleteTripMemberData, undefined>;

interface DeleteTripMemberRef {
  ...
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteTripMemberData, undefined>;
}
export const deleteTripMemberRef: DeleteTripMemberRef;
```
You can also pass in a `DataConnect` instance to the action shortcut function or `MutationRef` function.
```typescript
deleteTripMember(dc: DataConnect): MutationPromise<DeleteTripMemberData, undefined>;

interface DeleteTripMemberRef {
  ...
  (dc: DataConnect): MutationRef<DeleteTripMemberData, undefined>;
}
export const deleteTripMemberRef: DeleteTripMemberRef;
```

If you need the name of the operation without creating a ref, you can retrieve the operation name by calling the `operationName` property on the deleteTripMemberRef:
```typescript
const name = deleteTripMemberRef.operationName;
console.log(name);
```

### Variables
The `DeleteTripMember` mutation has no variables.
### Return Type
Recall that executing the `DeleteTripMember` mutation returns a `MutationPromise` that resolves to an object with a `data` property.

The `data` property is an object of type `DeleteTripMemberData`, which is defined in [dataconnect-generated/index.d.ts](./index.d.ts). It has the following fields:
```typescript
export interface DeleteTripMemberData {
  tripMember_delete?: TripMember_Key | null;
}
```
### Using `DeleteTripMember`'s action shortcut function

```typescript
import { getDataConnect } from 'firebase/data-connect';
import { connectorConfig, deleteTripMember } from '@dataconnect/generated';


// Call the `deleteTripMember()` function to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await deleteTripMember();

// You can also pass in a `DataConnect` instance to the action shortcut function.
const dataConnect = getDataConnect(connectorConfig);
const { data } = await deleteTripMember(dataConnect);

console.log(data.tripMember_delete);

// Or, you can use the `Promise` API.
deleteTripMember().then((response) => {
  const data = response.data;
  console.log(data.tripMember_delete);
});
```

### Using `DeleteTripMember`'s `MutationRef` function

```typescript
import { getDataConnect, executeMutation } from 'firebase/data-connect';
import { connectorConfig, deleteTripMemberRef } from '@dataconnect/generated';


// Call the `deleteTripMemberRef()` function to get a reference to the mutation.
const ref = deleteTripMemberRef();

// You can also pass in a `DataConnect` instance to the `MutationRef` function.
const dataConnect = getDataConnect(connectorConfig);
const ref = deleteTripMemberRef(dataConnect);

// Call `executeMutation()` on the reference to execute the mutation.
// You can use the `await` keyword to wait for the promise to resolve.
const { data } = await executeMutation(ref);

console.log(data.tripMember_delete);

// Or, you can use the `Promise` API.
executeMutation(ref).then((response) => {
  const data = response.data;
  console.log(data.tripMember_delete);
});
```

