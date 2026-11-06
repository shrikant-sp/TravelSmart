import { ConnectorConfig, DataConnect, QueryRef, QueryPromise, ExecuteQueryOptions, MutationRef, MutationPromise, DataConnectSettings } from 'firebase/data-connect';

export const connectorConfig: ConnectorConfig;
export const dataConnectSettings: DataConnectSettings;

export type TimestampString = string;
export type UUIDString = string;
export type Int64String = string;
export type DateString = string;




export interface Activity_Key {
  id: UUIDString;
  __typename?: 'Activity_Key';
}

export interface Booking_Key {
  id: UUIDString;
  __typename?: 'Booking_Key';
}

export interface CreateActivityData {
  activity_insert: Activity_Key;
}

export interface CreateBookingData {
  booking_insert: Booking_Key;
}

export interface CreateExpenseData {
  expense_insert: Expense_Key;
}

export interface CreateTripData {
  trip_insert: Trip_Key;
}

export interface CreateTripMemberData {
  tripMember_insert: TripMember_Key;
}

export interface CreateUserData {
  user_insert: User_Key;
}

export interface DeleteActivityData {
  activity_delete?: Activity_Key | null;
}

export interface DeleteBookingData {
  booking_delete?: Booking_Key | null;
}

export interface DeleteExpenseData {
  expense_delete?: Expense_Key | null;
}

export interface DeleteTripData {
  trip_delete?: Trip_Key | null;
}

export interface DeleteTripMemberData {
  tripMember_delete?: TripMember_Key | null;
}

export interface DeleteUserData {
  user_delete?: User_Key | null;
}

export interface Expense_Key {
  id: UUIDString;
  __typename?: 'Expense_Key';
}

export interface GetActivityData {
  activity?: {
    title: string;
    startTime: TimestampString;
  };
}

export interface GetBookingData {
  booking?: {
    providerName: string;
    cost?: number | null;
  };
}

export interface GetExpenseData {
  expense?: {
    amount: number;
    category: string;
  };
}

export interface GetTripData {
  trip?: {
    title: string;
    owner: {
      username: string;
    };
  };
}

export interface GetTripMemberData {
  tripMember?: {
    role?: string | null;
    user: {
      username: string;
    };
  };
}

export interface GetUserData {
  user?: {
    email: string;
    username: string;
  };
}

export interface ListActivitiesData {
  activities: ({
    title: string;
    locationName?: string | null;
  })[];
}

export interface ListBookingsData {
  bookings: ({
    type: string;
    providerName: string;
  })[];
}

export interface ListExpensesData {
  expenses: ({
    amount: number;
    category: string;
    payer?: {
      username: string;
    };
  })[];
}

export interface ListMyTripsData {
  trips: ({
    title: string;
  })[];
}

export interface ListTripMembersData {
  tripMembers: ({
    role?: string | null;
    user: {
      username: string;
    };
  })[];
}

export interface ListUsersData {
  users: ({
    username: string;
  })[];
}

export interface TripMember_Key {
  id: UUIDString;
  __typename?: 'TripMember_Key';
}

export interface Trip_Key {
  id: UUIDString;
  __typename?: 'Trip_Key';
}

export interface UpdateActivityData {
  activity_update?: Activity_Key | null;
}

export interface UpdateBookingData {
  booking_update?: Booking_Key | null;
}

export interface UpdateExpenseData {
  expense_update?: Expense_Key | null;
}

export interface UpdateTripData {
  trip_update?: Trip_Key | null;
}

export interface UpdateTripMemberData {
  tripMember_update?: TripMember_Key | null;
}

export interface UpdateUserData {
  user_update?: User_Key | null;
}

export interface User_Key {
  id: UUIDString;
  __typename?: 'User_Key';
}

interface CreateUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateUserData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateUserData, undefined>;
  operationName: string;
}
export const createUserRef: CreateUserRef;

export function createUser(): MutationPromise<CreateUserData, undefined>;
export function createUser(dc: DataConnect): MutationPromise<CreateUserData, undefined>;

interface UpdateUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateUserData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateUserData, undefined>;
  operationName: string;
}
export const updateUserRef: UpdateUserRef;

export function updateUser(): MutationPromise<UpdateUserData, undefined>;
export function updateUser(dc: DataConnect): MutationPromise<UpdateUserData, undefined>;

interface DeleteUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteUserData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteUserData, undefined>;
  operationName: string;
}
export const deleteUserRef: DeleteUserRef;

export function deleteUser(): MutationPromise<DeleteUserData, undefined>;
export function deleteUser(dc: DataConnect): MutationPromise<DeleteUserData, undefined>;

interface GetUserRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetUserData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetUserData, undefined>;
  operationName: string;
}
export const getUserRef: GetUserRef;

export function getUser(options?: ExecuteQueryOptions): QueryPromise<GetUserData, undefined>;
export function getUser(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetUserData, undefined>;

interface ListUsersRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListUsersData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListUsersData, undefined>;
  operationName: string;
}
export const listUsersRef: ListUsersRef;

export function listUsers(options?: ExecuteQueryOptions): QueryPromise<ListUsersData, undefined>;
export function listUsers(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListUsersData, undefined>;

interface CreateTripRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateTripData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateTripData, undefined>;
  operationName: string;
}
export const createTripRef: CreateTripRef;

export function createTrip(): MutationPromise<CreateTripData, undefined>;
export function createTrip(dc: DataConnect): MutationPromise<CreateTripData, undefined>;

interface UpdateTripRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateTripData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateTripData, undefined>;
  operationName: string;
}
export const updateTripRef: UpdateTripRef;

export function updateTrip(): MutationPromise<UpdateTripData, undefined>;
export function updateTrip(dc: DataConnect): MutationPromise<UpdateTripData, undefined>;

interface DeleteTripRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteTripData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteTripData, undefined>;
  operationName: string;
}
export const deleteTripRef: DeleteTripRef;

export function deleteTrip(): MutationPromise<DeleteTripData, undefined>;
export function deleteTrip(dc: DataConnect): MutationPromise<DeleteTripData, undefined>;

interface GetTripRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetTripData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetTripData, undefined>;
  operationName: string;
}
export const getTripRef: GetTripRef;

export function getTrip(options?: ExecuteQueryOptions): QueryPromise<GetTripData, undefined>;
export function getTrip(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetTripData, undefined>;

interface ListMyTripsRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListMyTripsData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListMyTripsData, undefined>;
  operationName: string;
}
export const listMyTripsRef: ListMyTripsRef;

export function listMyTrips(options?: ExecuteQueryOptions): QueryPromise<ListMyTripsData, undefined>;
export function listMyTrips(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListMyTripsData, undefined>;

interface CreateBookingRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateBookingData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateBookingData, undefined>;
  operationName: string;
}
export const createBookingRef: CreateBookingRef;

export function createBooking(): MutationPromise<CreateBookingData, undefined>;
export function createBooking(dc: DataConnect): MutationPromise<CreateBookingData, undefined>;

interface UpdateBookingRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateBookingData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateBookingData, undefined>;
  operationName: string;
}
export const updateBookingRef: UpdateBookingRef;

export function updateBooking(): MutationPromise<UpdateBookingData, undefined>;
export function updateBooking(dc: DataConnect): MutationPromise<UpdateBookingData, undefined>;

interface DeleteBookingRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteBookingData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteBookingData, undefined>;
  operationName: string;
}
export const deleteBookingRef: DeleteBookingRef;

export function deleteBooking(): MutationPromise<DeleteBookingData, undefined>;
export function deleteBooking(dc: DataConnect): MutationPromise<DeleteBookingData, undefined>;

interface GetBookingRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetBookingData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetBookingData, undefined>;
  operationName: string;
}
export const getBookingRef: GetBookingRef;

export function getBooking(options?: ExecuteQueryOptions): QueryPromise<GetBookingData, undefined>;
export function getBooking(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetBookingData, undefined>;

interface ListBookingsRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListBookingsData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListBookingsData, undefined>;
  operationName: string;
}
export const listBookingsRef: ListBookingsRef;

export function listBookings(options?: ExecuteQueryOptions): QueryPromise<ListBookingsData, undefined>;
export function listBookings(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListBookingsData, undefined>;

interface CreateActivityRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateActivityData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateActivityData, undefined>;
  operationName: string;
}
export const createActivityRef: CreateActivityRef;

export function createActivity(): MutationPromise<CreateActivityData, undefined>;
export function createActivity(dc: DataConnect): MutationPromise<CreateActivityData, undefined>;

interface UpdateActivityRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateActivityData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateActivityData, undefined>;
  operationName: string;
}
export const updateActivityRef: UpdateActivityRef;

export function updateActivity(): MutationPromise<UpdateActivityData, undefined>;
export function updateActivity(dc: DataConnect): MutationPromise<UpdateActivityData, undefined>;

interface DeleteActivityRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteActivityData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteActivityData, undefined>;
  operationName: string;
}
export const deleteActivityRef: DeleteActivityRef;

export function deleteActivity(): MutationPromise<DeleteActivityData, undefined>;
export function deleteActivity(dc: DataConnect): MutationPromise<DeleteActivityData, undefined>;

interface GetActivityRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetActivityData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetActivityData, undefined>;
  operationName: string;
}
export const getActivityRef: GetActivityRef;

export function getActivity(options?: ExecuteQueryOptions): QueryPromise<GetActivityData, undefined>;
export function getActivity(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetActivityData, undefined>;

interface ListActivitiesRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListActivitiesData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListActivitiesData, undefined>;
  operationName: string;
}
export const listActivitiesRef: ListActivitiesRef;

export function listActivities(options?: ExecuteQueryOptions): QueryPromise<ListActivitiesData, undefined>;
export function listActivities(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListActivitiesData, undefined>;

interface CreateExpenseRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateExpenseData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateExpenseData, undefined>;
  operationName: string;
}
export const createExpenseRef: CreateExpenseRef;

export function createExpense(): MutationPromise<CreateExpenseData, undefined>;
export function createExpense(dc: DataConnect): MutationPromise<CreateExpenseData, undefined>;

interface UpdateExpenseRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateExpenseData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateExpenseData, undefined>;
  operationName: string;
}
export const updateExpenseRef: UpdateExpenseRef;

export function updateExpense(): MutationPromise<UpdateExpenseData, undefined>;
export function updateExpense(dc: DataConnect): MutationPromise<UpdateExpenseData, undefined>;

interface DeleteExpenseRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteExpenseData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteExpenseData, undefined>;
  operationName: string;
}
export const deleteExpenseRef: DeleteExpenseRef;

export function deleteExpense(): MutationPromise<DeleteExpenseData, undefined>;
export function deleteExpense(dc: DataConnect): MutationPromise<DeleteExpenseData, undefined>;

interface GetExpenseRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetExpenseData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetExpenseData, undefined>;
  operationName: string;
}
export const getExpenseRef: GetExpenseRef;

export function getExpense(options?: ExecuteQueryOptions): QueryPromise<GetExpenseData, undefined>;
export function getExpense(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetExpenseData, undefined>;

interface ListExpensesRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListExpensesData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListExpensesData, undefined>;
  operationName: string;
}
export const listExpensesRef: ListExpensesRef;

export function listExpenses(options?: ExecuteQueryOptions): QueryPromise<ListExpensesData, undefined>;
export function listExpenses(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListExpensesData, undefined>;

interface CreateTripMemberRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<CreateTripMemberData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<CreateTripMemberData, undefined>;
  operationName: string;
}
export const createTripMemberRef: CreateTripMemberRef;

export function createTripMember(): MutationPromise<CreateTripMemberData, undefined>;
export function createTripMember(dc: DataConnect): MutationPromise<CreateTripMemberData, undefined>;

interface UpdateTripMemberRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<UpdateTripMemberData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<UpdateTripMemberData, undefined>;
  operationName: string;
}
export const updateTripMemberRef: UpdateTripMemberRef;

export function updateTripMember(): MutationPromise<UpdateTripMemberData, undefined>;
export function updateTripMember(dc: DataConnect): MutationPromise<UpdateTripMemberData, undefined>;

interface DeleteTripMemberRef {
  /* Allow users to create refs without passing in DataConnect */
  (): MutationRef<DeleteTripMemberData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): MutationRef<DeleteTripMemberData, undefined>;
  operationName: string;
}
export const deleteTripMemberRef: DeleteTripMemberRef;

export function deleteTripMember(): MutationPromise<DeleteTripMemberData, undefined>;
export function deleteTripMember(dc: DataConnect): MutationPromise<DeleteTripMemberData, undefined>;

interface GetTripMemberRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<GetTripMemberData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<GetTripMemberData, undefined>;
  operationName: string;
}
export const getTripMemberRef: GetTripMemberRef;

export function getTripMember(options?: ExecuteQueryOptions): QueryPromise<GetTripMemberData, undefined>;
export function getTripMember(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<GetTripMemberData, undefined>;

interface ListTripMembersRef {
  /* Allow users to create refs without passing in DataConnect */
  (): QueryRef<ListTripMembersData, undefined>;
  /* Allow users to pass in custom DataConnect instances */
  (dc: DataConnect): QueryRef<ListTripMembersData, undefined>;
  operationName: string;
}
export const listTripMembersRef: ListTripMembersRef;

export function listTripMembers(options?: ExecuteQueryOptions): QueryPromise<ListTripMembersData, undefined>;
export function listTripMembers(dc: DataConnect, options?: ExecuteQueryOptions): QueryPromise<ListTripMembersData, undefined>;

