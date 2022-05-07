import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Subcat2Component } from './subcat2.component';

describe('Subcat2Component', () => {
  let component: Subcat2Component;
  let fixture: ComponentFixture<Subcat2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Subcat2Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Subcat2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
