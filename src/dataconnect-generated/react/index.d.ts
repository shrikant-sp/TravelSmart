import { CreateUserData, UpdateUserData, DeleteUserData, GetUserData, ListUsersData, CreateTripData, UpdateTripData, DeleteTripData, GetTripData, ListMyTripsData, CreateBookingData, UpdateBookingData, DeleteBookingData, GetBookingData, ListBookingsData, CreateActivityData, UpdateActivityData, DeleteActivityData, GetActivityData, ListActivitiesData, CreateExpenseData, UpdateExpenseData, DeleteExpenseData, GetExpenseData, ListExpensesData, CreateTripMemberData, UpdateTripMemberData, DeleteTripMemberData, GetTripMemberData, ListTripMembersData } from '../';
import { UseDataConnectQueryResult, useDataConnectQueryOptions, UseDataConnectMutationResult, useDataConnectMutationOptions} from '@tanstack-query-firebase/react/data-connect';
import { UseQueryResult, UseMutationResult} from '@tanstack/react-query';
import { DataConnect } from 'firebase/data-connect';
import { FirebaseError } from 'firebase/app';


export function useCreateUser(options?: useDataConnectMutationOptions<CreateUserData, FirebaseError, void>): UseDataConnectMutationResult<CreateUserData, undefined>;
export function useCreateUser(dc: DataConnect, options?: useDataConnectMutationOptions<CreateUserData, FirebaseError, void>): UseDataConnectMutationResult<CreateUserData, undefined>;

export function useUpdateUser(options?: useDataConnectMutationOptions<UpdateUserData, FirebaseError, void>): UseDataConnectMutationResult<UpdateUserData, undefined>;
export function useUpdateUser(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateUserData, FirebaseError, void>): UseDataConnectMutationResult<UpdateUserData, undefined>;

export function useDeleteUser(options?: useDataConnectMutationOptions<DeleteUserData, FirebaseError, void>): UseDataConnectMutationResult<DeleteUserData, undefined>;
export function useDeleteUser(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteUserData, FirebaseError, void>): UseDataConnectMutationResult<DeleteUserData, undefined>;

export function useGetUser(options?: useDataConnectQueryOptions<GetUserData>): UseDataConnectQueryResult<GetUserData, undefined>;
export function useGetUser(dc: DataConnect, options?: useDataConnectQueryOptions<GetUserData>): UseDataConnectQueryResult<GetUserData, undefined>;

export function useListUsers(options?: useDataConnectQueryOptions<ListUsersData>): UseDataConnectQueryResult<ListUsersData, undefined>;
export function useListUsers(dc: DataConnect, options?: useDataConnectQueryOptions<ListUsersData>): UseDataConnectQueryResult<ListUsersData, undefined>;

export function useCreateTrip(options?: useDataConnectMutationOptions<CreateTripData, FirebaseError, void>): UseDataConnectMutationResult<CreateTripData, undefined>;
export function useCreateTrip(dc: DataConnect, options?: useDataConnectMutationOptions<CreateTripData, FirebaseError, void>): UseDataConnectMutationResult<CreateTripData, undefined>;

export function useUpdateTrip(options?: useDataConnectMutationOptions<UpdateTripData, FirebaseError, void>): UseDataConnectMutationResult<UpdateTripData, undefined>;
export function useUpdateTrip(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateTripData, FirebaseError, void>): UseDataConnectMutationResult<UpdateTripData, undefined>;

export function useDeleteTrip(options?: useDataConnectMutationOptions<DeleteTripData, FirebaseError, void>): UseDataConnectMutationResult<DeleteTripData, undefined>;
export function useDeleteTrip(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteTripData, FirebaseError, void>): UseDataConnectMutationResult<DeleteTripData, undefined>;

export function useGetTrip(options?: useDataConnectQueryOptions<GetTripData>): UseDataConnectQueryResult<GetTripData, undefined>;
export function useGetTrip(dc: DataConnect, options?: useDataConnectQueryOptions<GetTripData>): UseDataConnectQueryResult<GetTripData, undefined>;

export function useListMyTrips(options?: useDataConnectQueryOptions<ListMyTripsData>): UseDataConnectQueryResult<ListMyTripsData, undefined>;
export function useListMyTrips(dc: DataConnect, options?: useDataConnectQueryOptions<ListMyTripsData>): UseDataConnectQueryResult<ListMyTripsData, undefined>;

export function useCreateBooking(options?: useDataConnectMutationOptions<CreateBookingData, FirebaseError, void>): UseDataConnectMutationResult<CreateBookingData, undefined>;
export function useCreateBooking(dc: DataConnect, options?: useDataConnectMutationOptions<CreateBookingData, FirebaseError, void>): UseDataConnectMutationResult<CreateBookingData, undefined>;

export function useUpdateBooking(options?: useDataConnectMutationOptions<UpdateBookingData, FirebaseError, void>): UseDataConnectMutationResult<UpdateBookingData, undefined>;
export function useUpdateBooking(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateBookingData, FirebaseError, void>): UseDataConnectMutationResult<UpdateBookingData, undefined>;

export function useDeleteBooking(options?: useDataConnectMutationOptions<DeleteBookingData, FirebaseError, void>): UseDataConnectMutationResult<DeleteBookingData, undefined>;
export function useDeleteBooking(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteBookingData, FirebaseError, void>): UseDataConnectMutationResult<DeleteBookingData, undefined>;

export function useGetBooking(options?: useDataConnectQueryOptions<GetBookingData>): UseDataConnectQueryResult<GetBookingData, undefined>;
export function useGetBooking(dc: DataConnect, options?: useDataConnectQueryOptions<GetBookingData>): UseDataConnectQueryResult<GetBookingData, undefined>;

export function useListBookings(options?: useDataConnectQueryOptions<ListBookingsData>): UseDataConnectQueryResult<ListBookingsData, undefined>;
export function useListBookings(dc: DataConnect, options?: useDataConnectQueryOptions<ListBookingsData>): UseDataConnectQueryResult<ListBookingsData, undefined>;

export function useCreateActivity(options?: useDataConnectMutationOptions<CreateActivityData, FirebaseError, void>): UseDataConnectMutationResult<CreateActivityData, undefined>;
export function useCreateActivity(dc: DataConnect, options?: useDataConnectMutationOptions<CreateActivityData, FirebaseError, void>): UseDataConnectMutationResult<CreateActivityData, undefined>;

export function useUpdateActivity(options?: useDataConnectMutationOptions<UpdateActivityData, FirebaseError, void>): UseDataConnectMutationResult<UpdateActivityData, undefined>;
export function useUpdateActivity(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateActivityData, FirebaseError, void>): UseDataConnectMutationResult<UpdateActivityData, undefined>;

export function useDeleteActivity(options?: useDataConnectMutationOptions<DeleteActivityData, FirebaseError, void>): UseDataConnectMutationResult<DeleteActivityData, undefined>;
export function useDeleteActivity(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteActivityData, FirebaseError, void>): UseDataConnectMutationResult<DeleteActivityData, undefined>;

export function useGetActivity(options?: useDataConnectQueryOptions<GetActivityData>): UseDataConnectQueryResult<GetActivityData, undefined>;
export function useGetActivity(dc: DataConnect, options?: useDataConnectQueryOptions<GetActivityData>): UseDataConnectQueryResult<GetActivityData, undefined>;

export function useListActivities(options?: useDataConnectQueryOptions<ListActivitiesData>): UseDataConnectQueryResult<ListActivitiesData, undefined>;
export function useListActivities(dc: DataConnect, options?: useDataConnectQueryOptions<ListActivitiesData>): UseDataConnectQueryResult<ListActivitiesData, undefined>;

export function useCreateExpense(options?: useDataConnectMutationOptions<CreateExpenseData, FirebaseError, void>): UseDataConnectMutationResult<CreateExpenseData, undefined>;
export function useCreateExpense(dc: DataConnect, options?: useDataConnectMutationOptions<CreateExpenseData, FirebaseError, void>): UseDataConnectMutationResult<CreateExpenseData, undefined>;

export function useUpdateExpense(options?: useDataConnectMutationOptions<UpdateExpenseData, FirebaseError, void>): UseDataConnectMutationResult<UpdateExpenseData, undefined>;
export function useUpdateExpense(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateExpenseData, FirebaseError, void>): UseDataConnectMutationResult<UpdateExpenseData, undefined>;

export function useDeleteExpense(options?: useDataConnectMutationOptions<DeleteExpenseData, FirebaseError, void>): UseDataConnectMutationResult<DeleteExpenseData, undefined>;
export function useDeleteExpense(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteExpenseData, FirebaseError, void>): UseDataConnectMutationResult<DeleteExpenseData, undefined>;

export function useGetExpense(options?: useDataConnectQueryOptions<GetExpenseData>): UseDataConnectQueryResult<GetExpenseData, undefined>;
export function useGetExpense(dc: DataConnect, options?: useDataConnectQueryOptions<GetExpenseData>): UseDataConnectQueryResult<GetExpenseData, undefined>;

export function useListExpenses(options?: useDataConnectQueryOptions<ListExpensesData>): UseDataConnectQueryResult<ListExpensesData, undefined>;
export function useListExpenses(dc: DataConnect, options?: useDataConnectQueryOptions<ListExpensesData>): UseDataConnectQueryResult<ListExpensesData, undefined>;

export function useCreateTripMember(options?: useDataConnectMutationOptions<CreateTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<CreateTripMemberData, undefined>;
export function useCreateTripMember(dc: DataConnect, options?: useDataConnectMutationOptions<CreateTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<CreateTripMemberData, undefined>;

export function useUpdateTripMember(options?: useDataConnectMutationOptions<UpdateTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<UpdateTripMemberData, undefined>;
export function useUpdateTripMember(dc: DataConnect, options?: useDataConnectMutationOptions<UpdateTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<UpdateTripMemberData, undefined>;

export function useDeleteTripMember(options?: useDataConnectMutationOptions<DeleteTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<DeleteTripMemberData, undefined>;
export function useDeleteTripMember(dc: DataConnect, options?: useDataConnectMutationOptions<DeleteTripMemberData, FirebaseError, void>): UseDataConnectMutationResult<DeleteTripMemberData, undefined>;

export function useGetTripMember(options?: useDataConnectQueryOptions<GetTripMemberData>): UseDataConnectQueryResult<GetTripMemberData, undefined>;
export function useGetTripMember(dc: DataConnect, options?: useDataConnectQueryOptions<GetTripMemberData>): UseDataConnectQueryResult<GetTripMemberData, undefined>;

export function useListTripMembers(options?: useDataConnectQueryOptions<ListTripMembersData>): UseDataConnectQueryResult<ListTripMembersData, undefined>;
export function useListTripMembers(dc: DataConnect, options?: useDataConnectQueryOptions<ListTripMembersData>): UseDataConnectQueryResult<ListTripMembersData, undefined>;
