import { all, fork } from "redux-saga/effects"
import{
    watchJoin, watchLogin
} from "./userSaga"
import{
    watchWrite
} from "./articleSaga"

export default function* rootSaga(){
    yield all([ fork(watchJoin), fork(watchLogin), fork(watchWrite)])
}