import { configureStore } from '@reduxjs/toolkit'
import { fruitsSlice } from '../BlinkitProducts/Fruits'

export const store = configureStore({
  reducer: {
    fruits : fruitsSlice.reducer
  },
})