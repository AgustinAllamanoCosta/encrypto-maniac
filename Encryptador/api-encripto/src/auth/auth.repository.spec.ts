import { AuthRepository } from './auth.repository';

describe('AuthRepository', () => {
  it('should be defined', () => {
    expect(new AuthRepository()).toBeDefined();
  });
});
