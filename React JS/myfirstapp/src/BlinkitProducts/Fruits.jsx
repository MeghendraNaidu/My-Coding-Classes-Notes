import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  fruits: {
    apples : 10,
    bananas : 500
  },
}

export const fruitsSlice = createSlice({
  name: 'fruits',
  initialState,
  reducers: {
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1
    },
    decrement: (state) => {
      state.value -= 1
    },
    
  },
})
console.log(fruitsSlice)

// Action creators are generated for each case reducer function
export const { increment, decrement } = fruitsSlice.actions

export default fruitsSlice.reducer